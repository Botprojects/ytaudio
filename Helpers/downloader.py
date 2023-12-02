import io
import base64
from pytube import YouTube
from Helpers import cache

async def download (url, m):
    audio_cache = cache.get_cache(url)
            
    if not audio_cache:
        yt = YouTube(url)
        buffer = io.BytesIO()
        buffer.name = yt.title
        yt.streams.filter(only_audio = True).desc().first().stream_to_buffer(buffer)
        await m.reply_audio (buffer)
        cache.write_cache(url, buffer)

    else:
        buffer = io.BytesIO()
        buffer.name = audio_cache['title']
        buffer.seek(0)
        buffer.write(base64.b64decode(audio_cache['contents']))
        await m.reply_audio (buffer)
