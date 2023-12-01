import io
from pytube import YouTube

async def download (url, m):
    yt = YouTube(url)
    buffer = io.BytesIO()
    buffer.name = yt.title
    yt.streams.filter(only_audio = True).desc().first().stream_to_buffer(buffer)
    await m.reply_audio (buffer)
