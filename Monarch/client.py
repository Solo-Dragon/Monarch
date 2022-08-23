from pyrogram import Client
from Monarch import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME


bot = Client(
    ":mona:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "program"},
)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

calls = PyTgCalls(user, overload_quiet_mode=True)


with Client(":mon:", API_ID, API_HASH, bot_token=BOT_TOKEN) as sudo:
    me_bot = sudo.get_me()
with user as igris:
    me_user = igris.get_me()
