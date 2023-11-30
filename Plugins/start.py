from pyrogram import Client, filters


@Client.on_message(filters.command("start") & filters.private)
def handler (c, m):
    name = m.chat.first_name
    m.reply (
        f"Hello {name}, welcome to youtube audio downloader bot\nSend a youtube video link to extract the audio of that video"
    )
