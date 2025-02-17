from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        # Define the caption text
        caption = (
            f"<b>🤖 Bot :</b> <a href='https://t.me/Drax_Movie_Bot'>File Sharing Bot</a> \n"
            f"<b>📝 Language :</b> <a href='https://python.org'>Python 3</a> \n"
            f"<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n"
            f"<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a> \n"
            f"<b>📢 Channel :</b> <a href='https://t.me/DraX_Society'>Drax Society</a> \n"
            f"<b>🧑‍💻 Developer :</b> <a href='tg://user?id={OWNER_ID}'>DraX</a>"
        )

        # Send the image with the caption
        await client.send_photo(
            chat_id=query.message.chat.id,
            photo="https://ibb.co/bMJc7fHL",  # Replace with your image URL or file path
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            ),
            reply_to_message_id=query.message.message_id  # Reply to the original message
        )

        # Delete the original message (optional, if you want to replace it with the image)
        await query.message.delete()

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
