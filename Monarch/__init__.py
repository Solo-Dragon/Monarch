import os
from datetime import datetime
import importlib
from pyrogram import Client

StartTime = datetime.now()

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)

#BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

STRING_SESSION = os.environ.get("STRING_SESSION", None)
STRING_2 = os.environ.get("STRING_2", None)
STRING_3 = os.environ.get("STRING_3", None)
STRING_4 = os.environ.get("STRING_4", None)
STRING_5 = os.environ.get("STRING_5", None)

PREFIX = os.environ.get("PREFIX", ".")
OWNER_NAME = os.environ.get("OWNER_NAME", "Shadow Monarch")
SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID", -100))


UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO_URL", "https://github.com/Solo-Dragon/MonarchUB"
)

MONARCH_VERSION = "DEMON V2"
# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID") or 0)

# Load or No Load modules
#NO_LOAD = os.environ.get("NO_LOAD", "").split()

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = bool(os.environ.get("PM_AUTO_BAN", True))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))

# Custom Handler command
CMD_HANDLER = os.environ.get("CMD_HANDLER") or ","
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"$")

# Support
GROUP = os.environ.get("GROUP", "SoloGuild")
CHANNEL = os.environ.get("CHANNEL", "TheSungJinWoo")

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)





# Custom Name Sticker Pack
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

ALIVE_NAME = os.environ.get("ALIVE_NAME", "Igris")

ALIVE_LOGO = (
    os.environ.get("ALIVE_LOGO") or "https://images7.alphacoders.com/105/1054068.png"
)

INLINE_PIC = (
    os.environ.get("INLINE_PIC") or "https://telegra.ph/file/300c73b812eabf66985bc.jpg"
)

# Picture For VCPLUGIN
PLAY_PIC = (
    os.environ.get("PLAY_PIC") or "https://telegra.ph/file/b838a46ba3d33df83588d.jpg"
)

QUEUE_PIC = (
    os.environ.get("QUEUE_PIC") or "https://images6.alphacoders.com/105/1055057.png"
)

TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/") 
"""
# 'bot' variable
if STRING_SESSION:
    session = StringSession(str(STRING_SESSION))
else:
    session = "MonarchUB"
try:
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(bot)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()

if STRING_2:
    session2 = StringSession(str(STRING_2))
    Shadow2 = TelegramClient(
        session=session2,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py2 = PyTgCalls(MAN2)
else:
    call_py2 = None
    Shadow2 = None


if STRING_3:
    session3 = StringSession(str(STRING_3))
    Shadow3 = TelegramClient(
        session=session3,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py3 = PyTgCalls(MAN3)
else:
    call_py3 = None
    Shadow3 = None


if STRING_4:
    session4 = StringSession(str(STRING_4))
    Shadow4 = TelegramClient(
        session=session4,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py4 = PyTgCalls(MAN4)
else:
    call_py4 = None
    Shadow4 = None


if STRING_5:
    session5 = StringSession(str(STRING_5))
    Shadow5 = TelegramClient(
        session=session5,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py5 = PyTgCalls(MAN5)
else:
    call_py5 = None
    Shadow5 = None
"""
"""
async def update_restart_msg(chat_id, msg_id):
    message = (
        f"**Monarch v{BOT_VER} is back up and running!**\n\n"
        f"**Telethon:** {version.__version__}\n"
        f"**Python:** {python_version()}\n"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from userbot.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            LOOP.run_until_complete(update_restart_msg(int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass 
"""
# MONARCH = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

'''
PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

ub = Client(STRING_SESSION, API_ID, API_HASH, plugins=PLUGINS)'''
ub = Client(
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    session=STRING_SESSION,
)

MONARCH = Client('bot',
             api_id=os.environ.get('API_ID'),
             api_hash=os.environ['API_HASH'],
             bot_token=os.environ['TOKEN'],
             plugins=dict(root=f"{__name__}/plugins"))
# logging.basicConfig(level=logging.INFO)

""""
ub.start()
print('>>> USERBOT STARTED')
idle()
ub.stop()
print('\n>>> USERBOT STOPPED')"""
