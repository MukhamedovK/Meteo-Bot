from aiogram.types import *


async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("🌞 Погода сейчас"),
        KeyboardButton("🌅 На завтра"),
        KeyboardButton("🔮 На 5 дней"),
        KeyboardButton("🔮 На 10 дней"),
    )
    btn.row("🔔 Уведомления")
    btn.row("⚙️ Настройки")

    return btn


async def notification_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        InlineKeyboardButton("🌞 Прогноз на сегодня", callback_data="ib1"),
        InlineKeyboardButton("🌅 Прогноз на завтра", callback_data="ib2"),
        InlineKeyboardButton("🔮 На 5 дней", callback_data="ib3"),
        InlineKeyboardButton("🔮 На 10 дней", callback_data="ib4"),
    )

    return btn


async def unit_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        InlineKeyboardButton("🕗 Формат времени", callback_data="ib5"),
    )
    btn.add(
        InlineKeyboardButton("⚪️ 12-часовой", callback_data="ib6"),
        InlineKeyboardButton("🔘 24-часовой", callback_data="ib7"),
    )

    btn.add(
        InlineKeyboardButton("🌡 Температура", callback_data="ib8"),
    )
    btn.add(
        InlineKeyboardButton("🔘 °C", callback_data="ib9"),
        InlineKeyboardButton("⚪️ °F", callback_data="ib10"),
    )

    btn.add(
        InlineKeyboardButton("💨 Скорость ветра", callback_data="ib11"),
    )
    btn.add(
        InlineKeyboardButton("🔘 м/с", callback_data="ib12"),
        InlineKeyboardButton("⚪️ мили/ч", callback_data="ib13"),
    )

    btn.add(
        InlineKeyboardButton("💦 Осадки", callback_data="ib14"),
    )
    btn.add(
        InlineKeyboardButton("🔘 мм", callback_data="ib15"),
        InlineKeyboardButton("⚪️ дюймы", callback_data="ib16"),
    )

    btn.add(
        InlineKeyboardButton("⏱ Давление", callback_data="ib17"),
    )
    btn.add(
        InlineKeyboardButton("🔘 мм рт.ст.", callback_data="ib18"),
        InlineKeyboardButton("⚪️ дюймы рт.ст.", callback_data="ib19"),
    )
        
    return btn


async def settings_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("🌎 Изменить город")
    btn.add(
        KeyboardButton("📏 Единицы измерения"),
        KeyboardButton("🇷🇺/🇬🇧 Язык"),
    )
    btn.row("👥 Добавить бота в канал/группу")
    btn.row("↩️ Назад")

    return btn


async def city_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton("📍 Отправить геолокацию"),
        KeyboardButton("📝 Выбрать из 5-ти последних"),
        KeyboardButton("↩️ Назад"),
    )

    return btn


async def language_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton("🇷🇺 Русский"),
        KeyboardButton("🇬🇧 English"),
        KeyboardButton("↩️ Назад"),
    )

    return btn


async def invite_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton("👥 Добавить бота в группу"),
        KeyboardButton("📢 Добавить бота в канал"),
        KeyboardButton("↩️ Назад"),
    )

    return btn
