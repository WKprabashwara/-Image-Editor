# By @TroJanzHEX
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("âHá´Êá´", callback_data="help_data"),
                        InlineKeyboardButton("ðâð¨ AÊá´á´á´", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton("ð Sá´á´Êá´á´ á´á´á´á´", url="https://github.com/WKprabashwara/-Image-Editor"),
                    ],
                    [   
                        InlineKeyboardButton("ð¨âð» Dá´á´ á´Êá´á´á´Ê", url="https://t.me/Imprabashwara"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_text(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ð Bá´á´á´", callback_data="start_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ð Bá´á´á´", callback_data="start_data"),
                        InlineKeyboardButton("ð Sá´á´á´á´Êá´", url="https://t.me/ankivectorupdates"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception:
        pass
