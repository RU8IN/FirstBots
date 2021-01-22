from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FirstStates(StatesGroup):
    Start = State()
    Name = State()
    PhoneNumber = State()
    Else = State()