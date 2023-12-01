from pyrogram import Client, filters
from pyrogram.enums import MessageEntityType
from Helpers.custom_filters import url
from Helpers.downloader import download

@Client.on_message (filters.private & url)
async def handler (c, m):
    split_with_space = m.text.split(" ")
    split_with_newline = m.text.split("\n")
    urls = None
    # removes strings that does not starts with http:// or https://
    if len(split_with_newline) > len(split_with_space):
        urls = split_with_newline
    elif len(split_with_space) > len(split_with_newline):
        urls = split_with_space
    else:
        urls = split_with_space

    filtered_urls = [url for url in urls if url.startswith(("http://", "https://"))]
    
    count = 0
    status = """**Bulk Download**

    __Total__: {total}
    __Completed__: {completed}
    """
    status_msg = await m.reply(status.format(total = len(filtered_urls), completed = count))
    for url in filtered_urls:
        count += 1
        if len(urls) == 1:
            await m.reply("Extracting Audio")
            try:
                await download(url, m)
                await status_msg.edit_text(status.format(total = len(filtered_urls), completed = count))
            except:
                await m.reply(f"invalid url `{url}`")
        else:
            try:
                await download(url, m)
                await status_msg.edit_text(status.format(total = len(filtered_urls), completed = count))
            except Exception as e:
                await m.reply(f"invalid url `{url}`")
