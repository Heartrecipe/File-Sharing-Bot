#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href='tg://user?id={OWNER_ID}'>𝚃𝙷𝙸𝚂 𝙿𝙴𝚁𝚂𝙾𝙽</a>\n○ ✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : <code>Python3</code>\n○ ✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ ✯ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 : <a href='https://telegram.dog/heart_recipe'>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>\n○ ✯ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @VK_LINKZ\n○ ✯ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @heart_recipe</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
