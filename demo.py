from pyrogram import enums

@bot.on_message(filters.me & filters.command(["movie", "m"], [".", "!", "/"]))
async def movie_ul(bot, message):
 
    if len(message.command) == 1:
         return await message.edit('Give me movie name to search.')
            
    q = message.command[1:]
    query = listToString(q)
    
    data = []
    tata = []
    # Finding 100 files.
    async for x in bot.search_global(query=query + " " + "Hindi", filter=enums.MessagesFilter.DOCUMENT, limit=100):
        data.append(x)
    # Appending file_id and file_size in list.
    for x in range(len(data)):
        tata.append(dict({'file_size':data[x].document.file_size,'file_id':data[x].document.file_id}))

    # Quitting process if not find any files.
    if not data:
        return await message.edit(f'No Files Found named `{query}`. Successfully quited the process.')
    else:
        try:
            ok = [x['file_id'] for x in tata if x['file_size']==max([v['file_size'] for v in tata if v['file_size']<1073741824])][0]
            a = await bot.send_cached_media(chat_id='@HagadmabsaBot', file_id=ok)
            await a.reply('/dd')
            await asyncio.sleep(2)
            async for aa in bot.get_chat_history("@HagadmansaBot", 1):
                print(aa)
            await a.reply('/fs')
            await asyncio.sleep(2)
            async for aaa in bot.get_chat_history("@HagadmansaBot", 1):
                print(aaa)
        except:
            ok = [x['file_id'] for x in tata if x['file_size']==max([v['file_size'] for v in tata if v['file_size']<2147483648])][0]
            b = await bot.send_cached_media(chat_id='@HagadmabsaBot', file_id=ok)
            await b.reply('/dd')
            await asyncio.sleep(2)
            async for bb in bot.get_chat_history("@HagadmansaBot", 1):
                print(bb)
            await b.reply('/dd')
            await asyncio.sleep(2)
            async for bbb in bot.get_chat_history("@HagadmansaBot", 1):
                print(bbb)
