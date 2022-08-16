import asyncio
from pyrogram import enums

async for x in message._client.search_global(query='', filter=enums.MessagesFilter.DOCUMENT, limit=1):
    try:
       if (x.document.file_size >= 1073741824) and :
 await message.reply_cached_media(file_id=x.document.file_id, caption=x.document.file_name)
 await asyncio.sleep(0.5)
  
 
