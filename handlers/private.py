from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAx0CW1SIGwABBCNbYVhgeh82nsUhS6Ao0rPrp1eKIR8AAiQBAAJd9mBH4_VeoPoUqQ8eBA")
    await message.reply_text(
        f"""**Hey there! My name is Besties✨,
I can play music in your group🎉 .
ADD me in your group and play music freely🇮🇳 **
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Bot lists", url="https://t.me/BONDOFBESTIZZ")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/ELECTROBOT_SUPPORT"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ELECTRO_UPDATES"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add me to group ➕", url="https://t.me/BESTIES_ROBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Besties robot is online✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/BONDOFBESTIZZ")
                ]
            ]
        )
   )


