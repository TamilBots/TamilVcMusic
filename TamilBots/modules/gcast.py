import asyncio

from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Dialog
from pyrogram.types import Chat
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant

from TamilBots.services.callsmusic.callsmusic import client as USER
from TamilBots.config import SUDO_USERS


@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐆𝐜𝐚𝐬𝐭 🥳")
        if not message.reply_to_message:
            await lol.edit("❗ 𝐑𝐞𝐩𝐥𝐲 𝐓𝐨 𝐀𝐧𝐲 𝐓𝐞𝐱𝐭 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 𝐆𝐜𝐚𝐬𝐭!")
            return
        msg = message.reply_to_message.text
        async for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"𝗚𝗰𝗮𝘀𝘁𝗶𝗻𝗴.. 𝗦𝗲𝗻𝘁: {sent} 𝗰𝗵𝗮𝘁𝘀. 𝗙𝗮𝗶𝗹𝗲𝗱: {failed} 𝗖𝗵𝗮𝘁𝘀.")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                await lol.edit(f"𝗚𝗰𝗮𝘀𝘁𝗶𝗻𝗴.. 𝗦𝗲𝗻𝘁: {sent} 𝗰𝗵𝗮𝘁𝘀. 𝗙𝗮𝗶𝗹𝗲𝗱: {failed} 𝗖𝗵𝗮𝘁𝘀.")
                await asyncio.sleep(0.7)
                
        await message.reply_text(f"𝗚𝗰𝗮𝘀𝘁𝗶𝗻𝗴.. 𝗦𝗲𝗻𝘁: {sent} 𝗰𝗵𝗮𝘁𝘀. 𝗙𝗮𝗶𝗹𝗲𝗱: {failed} 𝗖𝗵𝗮𝘁𝘀.")
