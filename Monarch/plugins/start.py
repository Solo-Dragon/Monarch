from Monarch import MONARCH
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

MONARCH_START = """
I am Monarch [(신상)](https://mfiles.alphacoders.com/892/892886.png) `"Now it's time to worship God."` \n
**"He who fights with monsters\n, Should look to it that he himself does not become a monster. \n \nAnd if you gaze for long into an abyss, \nthe abyss gazes also into you.”**
This is Not your Bot 
My Owner is @SungJinWooX
Deploy Your Own From [here](https://github.com/Solo-Dragon)
"""
DEMON_MSG = """ 
Sung Jin-Woo (성진우) [Well it does'nt matter...](https://t.me/TheSungJinWoo) \n
**"I'm going to protect my family, even if it means turning all the hunters in the world against me."**
[성진우](https://static.wikia.nocookie.net/solo-leveling/images/5/54/Jinwoo13.jpg)
This is Not your Bot 
My Owner is @SungJinWooX
Deploy Your Own From [here](https://github.com/Solo-Dragon)
"""

@MONARCH.on_message(filters.command(["help"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Demon", url="https://t.me/SoloGuild"), InlineKeyboardButton("Creator", url = "https://t.me/SungJinWooX")],
                [InlineKeyboardButton("Off-Topic", url = "https://t.me/AnimeFunChat")]
              ]
    await MONARCH.send_message(chat_id = message.chat.id, text = MONARCH_START, reply_markup = InlineKeyboardMarkup(buttons))
    
    
@MONARCH.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Monarch Support", url="https://t.me/SoloGuild")],
                [InlineKeyboardButton("Add this Chatbot to your Group", url = "t.me/MonarchRobot?startgroup=true")]
              ]
    await MONARCH.send_message(chat_id = message.chat.id, text = DEMON_MSG, reply_markup = InlineKeyboardMarkup(buttons))
    
    
    
    
   # [@#$%](https://i.redd.it/8jyzn83m3k471.jpg)
