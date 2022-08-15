import os
from pyromod import listen
from pyrogram import Client

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")


bot = Client(":memory:",
      api_id=API_ID,
      api_hash=API_HASH,
      session_string=SESSION)
