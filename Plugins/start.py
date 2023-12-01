from pyrogram import Client, filters
from Helpers.buttons import start_button

@Client.on_message(filters.command("start") & filters.private)
async def handler (c, m):
    name = m.chat.first_name
    await m.reply (
        f"Hello {name}, welcome to youtube audio downloader bot\nSend a youtube video link to extract the audio of that video",
        reply_markup = start_button
    )
