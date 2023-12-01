from pyrogram import filters
from pyrogram.enums import MessageEntityType

async def filter_url (_, __, m):
    if not m.entities:
        return False

    for entity in m.entities:
        if entity.type == MessageEntityType.URL:
            return True

    return False

url = filters.create(filter_url)
