from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from AnonXMusic import userbot





@app.on_message(filters.command("vc", [".", "-", "!", "^", "/"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.command("bokep", [".", "-", "!", "^", "/"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
        


@app.on_message(filters.command("active", [".", "^", "-", "!", "/"]) & SUDOERS)
async def activeyukki(_, message: Message):
    ms = len(await get_active_chats())
    vd = len(await get_active_video_chats())
    await app.send_message(message.chat.id, 
        f"🎧 Active Chats:\n\n<b>• Music: {ms}</b>\n\n<b>• Stream: {vd}</b>")

@app.on_message(filters.command("ass", [".", "(", "-", "!", "/"]) & SUDOERS)
async def AnonXAss(_, message: Message):
    await userbot.one.send_message(message.chat.id, "Saya hadir tuan 😍")
    await userbot.two.send_message(message.chat.id, "Hadir ganteng 😝")
    await userbot.three.send_message(message.chat.id, "Hadir babang tampan 🤩")
    await userbot.four.send_message(message.chat.id, "Hadir dong mas bro 😘")
    await userbot.five.send_message(message.chat.id, "Hadir dong 👋")
