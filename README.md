[![Python Syntax Test](https://github.com/dartus95/fps_bot/actions/workflows/python-app.yml/badge.svg)](https://github.com/dartus95/fps_bot/actions/workflows/python-app.yml)
![Static Badge](https://img.shields.io/badge/Release%20Version-Version%201.1.0-brightgreen)
![Release](https://img.shields.io/github/v/release/dartus95/fps_bot?token=${{secrets.FPS_GITHUB_TOKEN}})

# FPS Discord Bot
FPS Clan has created this bot to save the mission file made by the mission maker without the hassle of logging into a remote Windows server or using programs such as AnyDesk, Teamviewer and else.

It aims to take a file sent to a specific discord channel as an attachment and save it into a specified directory on the server where the bot is running. So basically it can be used for other cases where uploading of files to a server would be normally too difficult or you do not want to give unnecessary access to someone.

## Features
List of features this bot can do:
* Upload mission file from specific discord channel to specified folder on windows serverr
* Confirm that file has been succesfully uploaded
* File type check - checking that file has correct file extension (.pbo)
* File size check - checking that file has correct file size (Default: 5MB)
* Discord command to check if bot is running (By default: !check)

## How-to
There are three things which need to be changed for it to be working properly:
* First you need to create a bot on the Discord Developer page - https://discord.com/developers/applications
    - You need to take the generated token and put it into .py file
    - You also need to invite the bot to your server
* Put channel ID into the .py file (there are plenty of guides how to get channel ID)
* Ensure that bot has rights to see specified discord channel
* Specify the path where the file will be saved (Do not forget to keep the double backslashes otherwise it won't work)
