import discord
import requests
import os
import shutil
from zipfile import ZipFile
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get token and guild ID from user input
TOKEN = input("Please enter your Discord token: ")
GUILD_ID = input("Please enter your Guild ID: ")

PNG_DIR = 'emojis/png'
GIF_DIR = 'emojis/gif'
ZIP_FILENAME = 'emojis.zip'

# Ensure the download directories exist
for directory in [PNG_DIR, GIF_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_emojis(emojis):
    for emoji in emojis:
        url = str(emoji.url)
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            ext = url.split('.')[-1]
            if ext == 'png':
                path = f"{PNG_DIR}/{emoji.name}.png"
            elif ext == 'gif':
                path = f"{GIF_DIR}/{emoji.name}.gif"
            else:
                continue
            with open(path, 'wb') as f:
                f.write(response.content)

def zip_emojis():
    with ZipFile(ZIP_FILENAME, 'w') as zipf:
        for root, dirs, files in os.walk('emojis'):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), 'emojis'))

def clean_up():
    shutil.rmtree('emojis')

intents = discord.Intents.default()
intents.emojis = True
intents.guilds = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    guild = discord.utils.get(client.guilds, id=int(GUILD_ID))
    if guild:
        print(f'Fetching emojis from: {guild.name}')
        download_emojis(guild.emojis)
        zip_emojis()
        clean_up()
        print('Emojis have been downloaded, zipped, and cleaned up successfully.')
    await client.close()

client.run(TOKEN, bot=False)