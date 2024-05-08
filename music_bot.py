##discord_music_bot playing music locally from your pc

import discord
from discord.ext import commands
import os
import asyncio

# Function to validate the token
def validate_token(token):
    # Ensure token is not empty
    if not token:
        return False
    
    # Add more validation criteria as needed
    # For example, checking length and character set
    if len(token) < 50:  # Assuming token length is at least 50 characters
        return False
    
    return True

# Function to get the token from environment variable or token file
def get_token():
    # Check if token is set as an environment variable
    token = os.getenv('DISCORD_TOKEN')
    if token and validate_token(token):
        print("Token found in environment variable.")
        return token

    # Check if token file exists
    token_file_path = "token.txt"
    if os.path.isfile(token_file_path):
        with open(token_file_path, "r") as file:
            token = file.read().strip()
            if validate_token(token):
                print("Token read from file:", token)
                return token
            else:
                print("Token file is empty or invalid.")

    # Prompt the user to input the token
    while True:
        token = input("Token not found or invalid. Enter your Discord token:")
        if validate_token(token):
            # Save the token to token file
            with open(token_file_path, "w") as file:
                file.write(token)
            print("Token saved to file.")
            return token
        else:
            print("Invalid token. Please enter a valid token.")

# Get the token
token = get_token()
print("Using token:", token)

# Function to validate the file path
def validate_file_path(f_path):
    # Add more validation criteria as needed
    if not os.path.isdir(f_path):
        return False
    
    return True

# Function to get the file path from file or user input
def get_file_path():
    # Check if file path file exists
    f_path_file_path = "file_path.txt"
    if os.path.isfile(f_path_file_path):
        with open(f_path_file_path, "r") as file:
            f_path = file.read().strip()
            if validate_file_path(f_path):
                print("File path read from file:", f_path)
                return f_path
            else:
                print("File path file is empty or invalid.")

    # Prompt the user to input the file path
    while True:
        f_path = input("File path not found or invalid. Please enter the path where your songs are saved:")
        if validate_file_path(f_path):
            # Save the file path to file
            with open(f_path_file_path, "w") as file:
                file.write(f_path)
            print("File path saved to file.")
            return f_path
        else:
            print("Invalid file path. Please enter a valid file path.")

# Get the file path
f_path = get_file_path()

# Restrict the bot's permissions within Discord
intents = discord.Intents.all()
intents.members = True  # Enable member intents for join and leave commands
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def join(ctx):
    if ctx.voice_client:
        await ctx.send("I'm already in a voice channel.")
        return

    if ctx.author.voice:
        channel = ctx.author.voice.channel
        try:
            await channel.connect()
        except discord.ClientException:
            await ctx.send("Failed to join the voice channel.")
    else:
        await ctx.send("You are not in a voice channel.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel.")

@bot.command()
async def play(ctx, *, song_name):
    if ctx.voice_client is None or not ctx.voice_client.is_connected():
        await ctx.send("Bot is not connected to a voice channel. Use the join command to connect.")
        return

    if ctx.voice_client.is_playing():
        await ctx.send("Audio is already playing.")
        return

    folder_path = f_path
    songs = os.listdir(folder_path)
    if not songs:
        await ctx.send("No songs found in the folder.")
        return

    matching_songs = [song for song in songs if song_name.lower() in song.lower()]
    if not matching_songs:
        await ctx.send(f"No song matching '{song_name}' found.")
        return

    file_path = os.path.join(folder_path, matching_songs[0])

    try:
        source = discord.FFmpegPCMAudio(file_path)
        ctx.voice_client.play(source)
        await asyncio.sleep(1)  # Delay to ensure the client has time to connect
        if not ctx.voice_client.is_connected():
            await ctx.send("Not connected to voice.")
            return
        await ctx.send(f'Now playing: {matching_songs[0]}')

        # Await until the playback ends
        while ctx.voice_client.is_playing():
            await asyncio.sleep(1)
        
    except FileNotFoundError:
        await ctx.send(f'File `{matching_songs[0]}` not found.')
    except discord.errors.ClientException:
        await ctx.send("Already playing audio.")
    except Exception as e:
        await ctx.send(f'An error occurred while playing the song: {e}')
        print("Error:", e)

@bot.command()
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Music stopped.")
    else:
        await ctx.send("No music is currently playing.")

@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Music resumed.")
    else:
        await ctx.send("No music to resume.")

try:
    bot.run(token)
except discord.errors.LoginFailure:
    print("Failed to log in. Please ensure that the token is correct.")
