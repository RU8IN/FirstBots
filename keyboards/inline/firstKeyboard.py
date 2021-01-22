from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FirstKeyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Начать", callback_data="start")
    ],
    [
        InlineKeyboardButton(text="Бесплатный", callback_data="Free"),
        InlineKeyboardButton(text="Ваш номер и email", callback_data="email")
    ]
], row_width=2)