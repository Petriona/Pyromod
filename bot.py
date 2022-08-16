import os
import io
import sys
import asyncio
import traceback
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
