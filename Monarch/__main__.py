from Monarch import MONARCH, ub
import os
from datetime import datetime
import importlib
#from MONARCH.MONARCH import MONARCH
#from MONARCH.MONARCH import start, MONARCH, MONARCHinline
from pyrogram import filters

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


def main():
    MONARCH.run()
    ub.start()
    print('>>> USERBOT STARTED')
    MONARCH.send_message(5378543429, "I'm awake... My Leige!!")


if __name__ == "__main__":
    main()

"""
if __name__ == "__main__":
    MONARCH.run()"""
