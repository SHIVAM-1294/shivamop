from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("vchelp") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""💞 Hello! Following are the commands available for **𝗘𝗟𝗘𝗖𝗧𝗥𝗢** - __A Group Voice Chat Music Player__.
The commands I currently support are:

🔥 **Users Commands :**
⚜️ /play - **[ Groups Only ]** > __Plays the replied audio file or YouTube video through link.__
⚜️ /song - **[ Groups & DM ]** > __Uploads the searched song in the chat.__



🔰 **Admin & Sudo Users Commands :**
⚜️ /pause - **[Groups Only ]** > __Pause Voice Chat Music.__
⚜️ /resume - **[Groups Only ]** > __Resume Voice Chat Music.__
⚜️ /skip - **[Groups Only ]** > __Skips the current Music Playing In Voice Chat.__
⚜️ /stop - **[Groups Only ]** > __Clears The Queue as well as ends Voice Chat Music.__""")

@Client.on_message(command("vchelp") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**𝗘𝗟𝗘𝗖𝗧𝗥𝗢 :-** Hey! PM me to get all the commands 😉")

