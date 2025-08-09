from pyrogram import Client, filters

from pyrogram.errors import (ChatAdminRequired, ChatWriteForbidden,

                             UserNotParticipant)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



from config import FSUB_IMG_URL, MUST_JOIN, OWNER_ANKES

from core import app

from strings import get_string

from utils.database import get_lang





@app.on_message(filters.incoming & filters.private, group=-1)

async def must_join_channel(app: Client, msg: Message):

    if not MUST_JOIN or MUST_JOIN is None:

        return

    user_id = msg.from_user.id if msg.from_user else None

    if not user_id:

        return

    language = await get_lang(msg.chat.id)

    _ = get_string(language)

    mention = await app.get_mention(msg)

    try:

        try:

            await app.get_chat_member(MUST_JOIN, user_id)

        except UserNotParticipant:

            if MUST_JOIN.isalpha():

                link = "https://t.me/" + MUST_JOIN

            else:

                chat_info = await app.get_chat(MUST_JOIN)

                link = chat_info.invite_link

            try:

                await msg.reply_photo(

                    photo=FSUB_IMG_URL,

                    caption=_["fsub_2"].format(mention, app.mention, OWNER_ANKES),

                    reply_markup=InlineKeyboardMarkup(

                        [

                            [

                                InlineKeyboardButton("❤️ Join", url=link),

                            ],

                                ),

                            ],

                        ]

                    ),

                )

                await msg.stop_propagation()

            except ChatWriteForbidden:

                pass

    except ChatAdminRequired:

        print(f"Promosi saya sebagai admin digrup/channels yang diFSUB: {MUST_JOIN} !")
