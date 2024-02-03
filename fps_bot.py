import os
import discord
from discord.ext import commands
import asyncio

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'
# Replace 'TARGET_CHANNEL_ID' with the ID of the text channel you want to monitor
TARGET_CHANNEL_ID = TARGET_CHANNEL_ID
# Replace 'TARGET_FOLDER' with the path to the folder where you want to save the files
TARGET_FOLDER = 'X:\\Your\\Target\\folder'


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
    # Get the target channel
    target_channel = bot.get_channel(TARGET_CHANNEL_ID)
    
    # Send a message to the target channel
    await target_channel.send('**FPS Bot**, se připojil! Nyní můžete nahrávat soubory s misemi.')

@bot.event
async def on_message(message):
    # Print details of new message detected in target channel
    print(f'Received message "{message.content}" in channel: {message.channel.name} (ID: {message.channel.id}) by {message.author.name} (ID: {message.author.id})')

    # Print message content and attachments for debugging purposes
    # print(f'Message content: {message.content}')
    # print(f'Message attachments: {message.attachments}')

    if message.channel.id == TARGET_CHANNEL_ID and message.attachments:
        # print(f'Detected new message with content: {message.content}')

        for attachment in message.attachments:
            # Pass the uploader's name to the save_attachment function
            await save_attachment(attachment, message.author.id)

            # Add a reaction after saving the attachment
            await message.add_reaction("✅")

    await bot.process_commands(message)


async def save_attachment(attachment, uploader_name):
    file_name = attachment.filename
    file_path = os.path.join(TARGET_FOLDER, file_name)

    content = await attachment.read()

    with open(file_path, 'wb') as file:
        file.write(content)

    print(f'Saved file: {file_name}')
    print(f'File size: {len(content)} bytes')

    # Send a message to channel with mention of uploader and the saved filename after it was processed
    channel = bot.get_channel(TARGET_CHANNEL_ID)
    await channel.send(f"<@{uploader_name}>, Mission file **__'{file_name}'__** byl úspěšně nahrán!")
    await channel.send(f"**---------------------- Nyní můžete nahrát další soubor ----------------------**")


async def main():
    await bot.start(TOKEN)

# Create a new event loop
loop = asyncio.new_event_loop()

# Set the event loop for the current thread
asyncio.set_event_loop(loop)

# Run the bot continuously
loop.run_until_complete(main())
