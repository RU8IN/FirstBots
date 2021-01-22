from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


FirstKeyboardDa = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Начать")
    ],
    [
        KeyboardButton(text="Бесплатный")
    ],
    [
        KeyboardButton(text="Телефон"),
        KeyboardButton(text="email")
    ]
], resize_keyboard=True, one_time_keyboard=True)