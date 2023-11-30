from pyrogram import Client
from config import *
Client (
    "ytaudio",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN,
    plugins = {
        "root": "Plugins"
    }
).run()
