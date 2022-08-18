import os
import io
import sys
import asyncio
import traceback
from pyrogram import enums
# from pyromod import listen
from pyrogram import Client, filters

NAME = "Pyromod"
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

bot = Client(
      name=NAME,
      api_id=API_ID,
      api_hash=API_HASH,
      session_string=SESSION
)

def listToString(s):
    str1 = " "
    return (str1.join(s))

@bot.on_message(filters.me & filters.command(["start"], [".", "!", "/"]))
async def start(bot, message):
  
 await message.edit('Hello')
      
@bot.on_message(filters.me & filters.document & filters.chat(-1001749789551))
async def start(bot, message):
  
 a = await bot.copy_message("HagadmansaBot", message.chat.id, message.id)
 await a.reply("/dd")
 await asyncio.sleep(2)
 async for b in bot.get_chat_history("HagadmansaBot", 1):
      print(b.text)
 await message.delete()
 await message.reply(b.text)
      
@bot.on_message(filters.me & filters.command(["movie", "m"], [".", "!", "/"]))
async def movie(bot, message):
      
     if len(message.command) == 1:
         return await message.edit('Give me movie name to search.')
            
     q = message.command[1:]
     query = listToString(q)
     data = []
    
     await message.edit('⏳ Running first process...')
 
     # Process of finding 1st file.
     async for x in bot.search_global(query=query + " " + "Hindi", filter=enums.MessagesFilter.DOCUMENT, limit=1):
        data.append(x)
        await bot.send_message(chat_id=-1001569147717, text=data)
     if not data:
       return await message.edit(f'No Files Found named `{query}`.')
     else:
       if (x.document.file_size < 1073741824) and (x.document.file_size > 536870912):      
          await message.edit('⏳ Running first process...\n- File Found. (0.5 GB to 1 GB)')
          a = await bot.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id, caption=x.document.file_name)
          await a.reply('/dd')
          await asyncio.sleep(2)
          async for aa in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (0.5 GB to 1 GB)\n- File Stream link generated.')
          await a.reply('/fs')
          await asyncio.sleep(2)
          async for aaa in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (0.5 GB to 1 GB)\n- File Stream link generated.\n- File Store link generated.')
          await asyncio.sleep(1)
          await message.edit('✅ First Process Comleted.')
            
       elif (x.document.file_size < 536870912):
          await message.edit('⏳ Running first process...\n- File Found. (less then 0.5 GB)')
          b = await bot.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id, caption=x.document.file_name)
          await b.reply('/dd')
          await asyncio.sleep(2)
          async for bb in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (less then 0.5 GB)\n- File Stream link generated.')
          await b.reply('/fs')
          await asyncio.sleep(2)
          async for bbb in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (less then 0.5 GB)\n- File Stream link generated.\n- File Store link generated.')
          await asyncio.sleep(1)
          await message.edit('✅ First Process Comleted.')
            
       elif (x.document.file_size < 1610612736) and (x.document.file_size > 1073741824):
          await message.edit('⏳ Running first process...\n- File Found. (1 GB to 1.5 GB)')
          c = await bot.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id, caption=x.document.file_name)
          await c.reply('/dd')
          await asyncio.sleep(2)
          async for cc in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (1 GB to 1.5 GB)\n- File Stream link generated.')
          await c.reply('/fs')
          await asyncio.sleep(2)
          async for ccc in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (1 GB to 1.5 GB)\n- File Stream link generated.\n- File Store link generated.')
          await asyncio.sleep(1)
          await message.edit('✅ First Process Comleted.')
            
       elif (x.document.file_size < 2147483648) and (x.document.file_size > 1610612736):
          await message.edit('⏳ Running first process...\n- File Found. (1.5 GB to 2 GB)')
          d = await bot.send_cached_media(chat_id="@HagadmansaBot", file_id=x.document.file_id, caption=x.document.file_name)
          await d.reply('/dd')
          await asyncio.sleep(2)
          async for dd in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (1.5 GB to 2 GB)\n- File Stream link generated.')
          await d.reply('/fs')
          await asyncio.sleep(2)
          async for ddd in bot.get_chat_history("@HagadmansaBot", 1):
            await message.edit('⏳ Running first process...\n- File Found. (1.5 GB to 2 GB)\n- File Stream link generated.\n- File Store link generated.')
          await asyncio.sleep(1)
          await message.edit('✅ First Process Comleted.')
            
     # await message.edit('Done, published on website.')

@bot.on_message(filters.me & filters.command(["k"], [".", "!", "/"]))
async def movie_ul(bot, message):
 
    if len(message.command) == 1:
         return await message.edit('Give me movie name to search.')

    await message.edit('Just Wait A minute brother')
            
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
            a = await bot.send_cached_media(chat_id='@HagadmansaBot', file_id=ok)
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
            b = await bot.send_cached_media(chat_id='@HagadmansaBot', file_id=ok)
            await b.reply('/dd')
            await asyncio.sleep(2)
            async for bb in bot.get_chat_history("@HagadmansaBot", 1):
                print(bb)
            await b.reply('/dd')
            await asyncio.sleep(2)
            async for bbb in bot.get_chat_history("@HagadmansaBot", 1):
                print(bbb)
            
@bot.on_message(filters.me & filters.command(["eval"], [".", "!", "/"]))
async def eval(bot, message):
      
    cmd = message.text.split(" ", maxsplit=1)[1]

    await message.edit("Processing ...")

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, bot, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await message.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1]
            )
            await message.delete()
    else:
        await message.edit(final_output)


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

if __name__ == "__main__":    
 bot.run()
