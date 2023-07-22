import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.types import *
from btn import start_btn, notification_btn, settings_btn, city_btn, language_btn, invite_btn, unit_btn

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "5935940670:AAFazHO96cj2dNOd5a1c0uK_mlBnH84IGhQ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    btn = await start_btn()
    await message.answer(f"Здравствуйте, {message.from_user.mention}", reply_markup=btn)


@dp.message_handler()
async def text_handler(message: Message):
    text = message.text
    if text == "🔔 Уведомления":
        btn = await notification_btn()
        await message.answer("Выберите тип отправляемых уведомлений:", reply_markup=btn)

    elif text == "⚙️ Настройки":
        btn = await settings_btn()
        await message.answer("Настройки", reply_markup=btn)

    elif text == "↩️ Назад":
        btn = await start_btn()
        await message.answer("Вот список того, что я умею:", reply_markup=btn)

    elif text == "🌎 Изменить город":
        btn = await city_btn()
        await message.answer("Напишите название населенного пункта или отправь свою геолокацию, чтобы я показал тебе погоду:", reply_markup=btn)
        
    elif text == "📏 Единицы измерения":
        btn = await unit_btn()
        await message.answer("Единицы измерения:", reply_markup=btn)

    elif text == "🇷🇺/🇬🇧 Язык":
        btn = await language_btn()
        await message.answer("Выберите язык / Choose language", reply_markup=btn)

    elif text == "👥 Добавить бота в канал/группу":
        btn = await invite_btn()
        await message.answer("Выберите действие:", reply_markup=btn)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
