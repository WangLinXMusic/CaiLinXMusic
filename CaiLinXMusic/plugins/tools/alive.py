import asyncio

from CaiLinXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://files.catbox.moe/vpehu4.jpg",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text=" ꜱᴀꜱᴜᴋᴇ  ", url=f"https://t.me/ZuriOfficialBoy"
            ),
            InlineKeyboardButton(
                text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/ZuriOfficialUpgrade"
            ),
        ],
                [
            InlineKeyboardButton(
                text=" ᴄʜᴀɴɴᴇʟ ", url=f"https://t.me/ZuriOfficialUpdate"
            ),
                ],
                [
                    InlineKeyboardButton(
                        " ᴄʟᴏsᴇ ", callback_data="close"
                    )
                ],
            ]
        )
    )
