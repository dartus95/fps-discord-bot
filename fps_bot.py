import os
import discord
from datetime import datetime, UTC
from discord.ext import commands
import asyncio

# Replace 'BOT_TOKEN_ID' with your actual bot token
TOKEN = 'BOT_TOKEN_ID'
# Replace 'CHANNEL_ID' with the ID of the text channel you want to monitor
TARGET_CHANNEL_ID = CHANNEL_ID
# Replace 'TARGET_FOLDER' with the path to the folder where you want to save the files in following format: X:\\Your\\Target\\folder
TARGET_FOLDER = 'MISSION_FILE_PATH'


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
    # Ignoruj zprávy z jiných kanálů než cílového
    if message.channel.id != TARGET_CHANNEL_ID:
        return
    
    # Print details of new message detected in target channel
    print(f'Received message "{message.content}" in channel: {message.channel.name} (ID: {message.channel.id}) by {message.author.name} (ID: {message.author.id})')

    # Print message content and attachments for debugging purposes
    # print(f'Message content: {message.content}')
    # print(f'Message attachments: {message.attachments}')

    if message.channel.id == TARGET_CHANNEL_ID and message.attachments:
        # print(f'Detected new message with content: {message.content}')

        for attachment in message.attachments:
            # KONTROLA FORMÁTU - povolení pouze .pbo souborů
            if not attachment.filename.lower().endswith('.pbo'):
                await message.channel.send(f"<@{message.author.id}>, Chyba: Povoleny jsou pouze .pbo soubory!")
                await message.add_reaction("❌")
                continue  # Přeskočí neplatný soubor

            # KONTROLA VELIKOSTI - maximálně 5MB
            MAX_SIZE_MB = 5
            if attachment.size > 5 * 1024 * 1024:  # 5MB v bytech
                await message.channel.send(
                    f"<@{message.author.id}>, Soubor '{attachment.filename}' přesahuje {MAX_SIZE_MB}MB! Prosím kontaktuj správce serveru!"
                )
                await message.add_reaction("❌")
                continue
                # Pokud projde kontrolami, pokračuje v uložení
            
            # Pass the uploader's name to the save_attachment function
            await save_attachment(attachment, message.author.id)

            # Add a reaction after saving the attachment
            await message.add_reaction("✅")

    await bot.process_commands(message)

@bot.command(name='check')
async def check_bot_status(ctx):
    # Logování do konzole
    print(f'Status check proveden uživatelem: {ctx.author.name} ({ctx.author.id})')
    
    # Výpočet doby běhu
    current_time = datetime.now(UTC)
    uptime = current_time - bot.user.created_at.replace(tzinfo=UTC)
    uptime_str = str(uptime).split('.')[0]  # Odstraní mikrosekundy

    # Odezva v Discordu
    embed = discord.Embed(
        title="🟢 BOT JE ONLINE",
        description=f"Bot běží správně",
        color=0x00ff00
    )
    # embed.add_field(name="Doba běhu", value=uptime_str, inline=False)
    embed.add_field(name="Ping", value=f"{round(bot.latency * 1000)}ms", inline=False)
    embed.set_footer(text=f"Požadavek od: {ctx.author.name}")
    
    await ctx.send(embed=embed)

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
