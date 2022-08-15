from bot import bot
from pyromod import listen
from pyrogram import Client, filters

# @bot.on_message(filters.private & filters.command("start"))
# async def genStr(bt, msg):
  
#   hemlo = await msg.reply('Hello')
#   api = await bot.ask(msg.chat.id, "How are you bruh?")
#   await hemlo.edit(api.text)

@bot.on_message(filters.me & filters.document & filters.chat(-1001749789551))
async def start(bt, message):
  
  a = await bt.copy_message("HagadmansaBot", message.chat.id, message.id)
  await a.reply("/dd")
  b = bt.get_chat_history("HagadmansaBot", 1)
  await message.delete()
  await message.reply(b.text)
  
  
  #api = await bot.ask(message.chat.id, "How are you bruh?")
  #await message.edit(api.text)
  #await api.delete()
  
if __name__ == "__main__":
    bot.run()
