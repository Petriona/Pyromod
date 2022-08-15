import os
# from pyromod import listen
from pyrogram import Client

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

@Client.on_message(filters.me & filters.document & filters.chat(-1001749789551))
async def start(bot, message):
  
  a = await bot.copy_message("HagadmansaBot", message.chat.id, message.id)
  await a.reply("/dd")
  b = bot.get_chat_history("HagadmansaBot", 1)
  print(b)
  await message.delete()
  await message.reply(b.text)

# if __name__ == "__main__":    
bot.run()
