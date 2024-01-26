from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import executor
from .models import Just
from django.conf import settings
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
from channels.db import database_sync_to_async
bot = Bot(token="1289185931:AAEGdoVik_p5rXlg1eQP8AZtMJ7er3-m4mw")
dp = Dispatcher(bot)

@database_sync_to_async
def get_just_objects():
    return list(Just.objects.all())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    buttons = [
        InlineKeyboardButton(text=f"☎️Телефоны/Адреса", callback_data=f"☎️Телефоны/Адреса")


    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.answer("Нажмите на нужную кнопку ⬇️", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: True)
async def handle_buttons(callback_query: types.CallbackQuery):
    # Handle button callbacks here based on the callback_data
    items=await get_just_objects()

    callback_data = callback_query.data
    buttons=[]
    if callback_data == "☎️Телефоны/Адреса":
        for item in items:
            buttons.append(InlineKeyboardButton(text=f"{item.name}", callback_data=f"{item.name}"))

        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(*buttons)
        await bot.edit_message_reply_markup(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            reply_markup=keyboard
        )








# ... add more event handlers as needed ...


