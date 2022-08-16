import asyncio
from pyrogram import enums

async for x in message._client.search_global(query='morbius 2022 hindi', filter=enums.MessagesFilter.DOCUMENT, limit=1):
    if len(x) == 0:
        return await message.edit('No Files Found')
    
    try:
       if (x.document.file_size < 2147483648) and (x.document.file_size > 1610612736):
          a = await message._client.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id)
          await a.reply('/dd')
          await asyncio.sleep(2)
          async for aa in bot.get_chat_history("@HagadmansaBot", 1):
            print(aa.text)
          await a.reply('/fs')
          await asyncio.sleep(2)
          async for aaa in bot.get_chat_history("@HagadmansaBot", 1):
            print(aaa.text)
       elif (x.document.file_size < 1610612736) and (x.document.file_size > 1073741824):
          b = await message._client.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id)
          await b.reply('/dd')
          await asyncio.sleep(2)
          async for bb in bot.get_chat_history("@HagadmansaBot", 1):
            print(bb.text)
          await b.reply('/fs')
          await asyncio.sleep(2)
          async for bbb in bot.get_chat_history("@HagadmansaBot", 1):
            print(bbb.text)
          await b.reply('/dd')
       elif (x.document.file_size < 1073741824) and (x.document.file_size > 536870912):
          c = await message._client.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id)
          await c.reply('/dd')
          await asyncio.sleep(2)
          async for cc in bot.get_chat_history("@HagadmansaBot", 1):
            print(cc.text)
          await c.reply('/fs')
          await asyncio.sleep(2)
          async for ccc in bot.get_chat_history("@HagadmansaBot", 1):
            print(ccc.text)
       elif (x.document.file_size < 536870912):
          d = await message._client.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id)
          await d.reply('/dd')
          await asyncio.sleep(2)
          async for dd in bot.get_chat_history("@HagadmansaBot", 1):
            print(dd.text)
          await d.reply('/fs')
          await asyncio.sleep(2)
          async for ddd in bot.get_chat_history("@HagadmansaBot", 1):
            print(ddd.text)
       else:
          await message.edit('No file found')
    except Exception as e:
       await message.edit(e)
