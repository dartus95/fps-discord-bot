# FPS Discord Bot
FPS Clan has created this bot to save the mission file made by the mission maker without the hassle of logging into a remote server or using programs such as AnyDesk, Teamviewer and else.

It aims to take a file sent to a specific discord channel as an attachment and save it into a specified directory on the server where the bot is running. So basically it can be used for other cases where uploading of files to a server would be normally too difficult or you do not want to give unnecessary access to someone.

## How-to
There are three things which need to be changed for it to be working properly:
* First you need to create a bot on the Discord Developer page - https://discord.com/developers/applications
    - You need to take the generated token and put it into .py file
    - You also need to invite the bot to your server
* Put channel ID into the .py file (there are plenty of guides how to get channel ID)
* Specify the path where the file will be saved (Do not forget to keep the double backslashes otherwise it won't work)
