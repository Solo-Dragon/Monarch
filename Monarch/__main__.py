from Monarch import MONARCH, ub, botx
import os
from datetime import datetime
import importlib
#from MONARCH.MONARCH import MONARCH
#from MONARCH.MONARCH import start, MONARCH, MONARCHinline
from pyrogram import Client, filters, idle
from Monarch.client import bot, user


from apscheduler.schedulers.asyncio import AsyncIOScheduler

import logging
"""
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - [MonarchUB] - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
"""
StartTime = datetime.now()

def load_cmds(ALL_PLUGINS):
    for oof in ALL_PLUGINS:
        if oof.lower() == "help":
            continue
        imported_module = importlib.import_module("Monarch.plugins." + oof)
        if not hasattr(imported_module, "__PLUGIN__"):
            imported_module.__PLUGIN__ = imported_module.__name__

        if not imported_module.__PLUGIN__.lower() in HELP_COMMANDS:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one"
            )

        if hasattr(imported_module, "__help__") and imported_module.__help__:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module.__help__
    return "Done Loading Plugins and Commands!"


logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s - [MonarchUB] - %(levelname)s - %(message)s",
    #format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)
"""
if not STRING_SESSION:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not MONGO_DB:
    logging.error("No MongoDB Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)
"""
scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

botx.start()
botx.join_chat("TheSoloGuild")

def main():
    MONARCH.run()
    ub.start()
    botx.start()
    botx.join_chat("TheSoloGuild")
    print('>>> USERBOT STARTED')
    botx.send_message("TheSoloGuild", "I'm awake")
    MONARCH.send_message(-1001755588048, "I'm awake... My Leige!!")
    
async def start_bot():
    await bot.start()
    LOGS.info("[INFO]: BOT & USERBOT CLIENT STARTED !!")
    await user.join_chat("KazutoSupport")
    await user.join_chat("AinCradNetwork")
    await user.join_chat("TheSoloGuild")
    await idle()
    LOGS.info("[INFO]: BOT & USERBOT STOPPED !!")
    await bot.stop()
    
if __name__ == "__main__":
    main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    print("Monarch is Alive")
    print("For Help Visit @TheSoloGuild")
    


    
    

"""
if __name__ == "__main__":
    MONARCH.run()"""
