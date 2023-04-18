# discord bot that waits for midjourney to generate the image,
#     and get it's url
from discord.ext import commands
import discord
import json

secret = json.load(open("secret.json"))
MJ_CHANNEL = 1068776705042415629
API_KEY = secret["ds_key"]


class MyClient(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("bot ready")
        channel = bot.get_channel(MJ_CHANNEL)

    async def on_message(self, message):
        if message.attachments:
            print(message.attachments[0].url) #just send url to cout


intents = discord.Intents.all()
intents.reactions = True
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True
bot = MyClient(command_prefix='!', intents=intents)
bot.run(API_KEY)
