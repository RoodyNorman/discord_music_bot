Project Title: Discord_music_bot

Creator: RoodyNorman 

Description:
This Discord bot allows users to play music in voice channels by using simple commands. It provides features such as joining voice channels, playing, resuming, and stopping music playback.

Features:
- Join voice channel command
- Play music command
- Resume, and stop music playback commands
- Error handling for common scenarios
- Enhanced security measures for token handling

Installation:
1. Requirements:
   - Python 3.6 or higher
   - discord.py library
   - FFmpeg

2. Installation Steps:
   - Install Python: https://www.python.org/downloads/
   - Install FFmpeg: https://ffmpeg.org/download.html
   1) Install the script as a zip file :
      -Extract the files 
      -Run music_bot.py
   2) Install with git :
      -Clone the repository: git clone https://github.com/RoodyNorman/discord_music_bot.git
      -cd discord_music_bot
      -python music_bot.py

3. Configuration:
   - Create a Discord bot and obtain its token from the Discord Developer Portal.
   - Set up environment variable DISCORD_TOKEN with your bot token.

4. Invite the bot to your Discord server using the invite link generated in the [Discord Developer Portal](https://discord.com/developers/applications).

## Commands
- `!join`: Join the voice channel the user is currently in.
- `!leave`: Leave the current voice channel.
- `!play <song_name>`: Play a song with the given name in the voice channel.
- `!stop`: Stop the currently playing song.
- `!resume`: Resume playback of a paused song.

## Contributing
Contributions are welcome! If you have suggestions for improvements, please open an issue or create a pull request on GitHub.

## License
This project is licensed under the MIT License - see the [LICENSE.txt] file for details.

Usage:
- Use the "!join" command to make the bot join your voice channel.
- Use the "!play <song_name>" command to play a specific song.
- Use the "!resume", and "!stop" commands to control music playback.

- In order to use this script you must have the songs you want to play downloaded in .mp3 format inside a file locally on your pc.
- Make sure they are saved in the same directory and path as your music_bot.py otherwise the script is not going to work.

Security Considerations:
- Input validation and error handling mechanisms are implemented to prevent injection attacks and handle unexpected scenarios.
- Tokens are retrieved securely from environment variables to avoid exposing sensitive information.

Troubleshooting:
- If the bot is not responding, ensure that it has the necessary permissions and is correctly configured with the bot token.
- Check the console for error messages, and refer to the Troubleshooting section of the README for solutions to common issues.
- Make sure the bot has all the necessary permissions to properly run in your discord server and in your voice channel.
- Make sure you have saved the songs you want to play in .mp3 format and saved in a file in the same directory and path as the music_bot.py otherwise the script will fail.
- The "!resume" command is still under development and it may not work . 

Contributing:
- Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request on GitHub.

License:
This project is licensed under the MIT License. See the LICENSE file for details.

Contact Information:
For questions or feedback, contact us at:
- Email: roodynorman@gmail.com
- Discord: discordapp.com/users/912366817266249769

Acknowledgements:
- Special thanks to the discord.py and FFmpeg communities for their support and contributions.

Version History:
- v1.0 (Initial Release): Basic bot functionality with music playback commands and decent security.

References:
- discord.py documentation: https://discordpy.readthedocs.io/en/stable/
- FFmpeg: https://ffmpeg.org/
