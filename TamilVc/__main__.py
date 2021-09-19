import requests
from pyrogram import Client as Bot

from TamilVc.config import API_HASH
from TamilVc.config import API_ID
from TamilVc.config import BG_IMAGE
from TamilVc.config import BOT_TOKEN
from TamilVc.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="TamilVc.modules"),
)

bot.start()
run()
