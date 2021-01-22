from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class send_news(StatesGroup):
    send_news_waiting_for_answer = State()
    send_news_waiting_for_message = State()
    send_news_waiting_for_photo = State()
    send_news_final = State()
    Else = State()