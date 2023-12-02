import json
import base64
from pydub import AudioSegment

PATH = "Helpers/cache.json"

def get_cache (url):
    with open (PATH, "r") as f:
        file = json.load(f)
    
    if file.get(url):
        return file.get(url)
    else:
        return False

def write_cache(url, buffer):
    with open (PATH, "r") as f:
        file = json.load(f)

    buffer.seek(0)

    encoded_audio = base64.b64encode(buffer.read()).decode("utf-8")
    
    
    data = {
        "title": buffer.name,
        "contents": encoded_audio
    }

    print(data)

    file[url] = data

    with open (PATH, "w") as f:
        json.dump(file, f, indent = 4)
