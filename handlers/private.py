from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("")
    await message.reply_text(
        f"""**Hello, I'm {bn} 🎙
𝐈 𝐂𝐚𝐧 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭.
𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐅𝐫𝐞𝐞𝐥𝐲... 🤗\n\n  💠 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : [TamilBots 🤖](https://t.me/TamilBots)!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨🏻‍💻 𝑺𝒐𝒖𝒓𝒄𝒆 𝑪𝒐𝒅𝒆 👨🏻‍💻", url="https://github.com/TamilBots/TamilVcMusic")
                  ],[
                    InlineKeyboardButton(
                        "😊 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 😊", url="https://t.me/TamilSupport"
                    ),
                    InlineKeyboardButton(
                        "📢 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 📢", url="https://t.me/thewarbotz"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕𝑨𝒅𝒅 𝑴𝒆 𝑻𝒐 𝒀𝒐𝒖𝒓 𝑮𝒓𝒐𝒖𝒑➕", url="https://t.me/Tamilinibot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝚈𝚎𝚜 𝚒𝚖 𝚘𝚗𝚕𝚒𝚗𝚎 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 📢", url="https://t.me/TamilBots")
                ]
            ]
        )
   )
