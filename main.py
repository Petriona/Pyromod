from bot import bot
from pyromod import listen
from pyrogram import Client, filters

@bot.on_message(filters.private & filters.command("start"))
async def genStr(bt, msg):
  
  hemlo = await message.reply('Hello')
  api = await bot.ask(message.chat.id, "How are you bruh?")
  await hemlo.edit(api.text)
  
if __name__ == "__main__":
    bot.run()
