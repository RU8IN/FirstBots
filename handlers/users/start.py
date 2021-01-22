import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import admins
from loader import dp, bot
from states import MainStates
from utils.misc import rate_limit


@rate_limit(5, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if str(message.from_user.id) not in open('data/users_ids.txt').read():
        file = open('data/users_ids.txt', 'a')
        file.write(str(message.from_user.id) + '\n')
        file.close()

    await message.answer(f'Привет! Здесь Вы можете получить своё предсказание!', reply_markup=None)
    time.sleep(1)
    await message.answer(text="Пожалуйста, введите своё имя: ")
    await MainStates.FirstStates.PhoneNumber.set()


@dp.message_handler(state=MainStates.FirstStates.PhoneNumber, content_types=types.ContentTypes.TEXT)
async def name_question(message: types.Message, state: FSMContext):
    await message.answer(text="Пожалуйста, введите свой номер телефона: ")
    await state.update_data(person_name=message.text)
    await MainStates.FirstStates.Else.set()


@dp.message_handler(state=MainStates.FirstStates.Else, content_types=types.ContentTypes.TEXT)
async def phone_number_question(message: types.Message, state: FSMContext):
    await message.answer("Хорошо, скоро Вам пришлют предсказание.")
    await state.update_data(person_number=message.text)
    user_data = await state.get_data()
    for admin in admins:
        await bot.send_message(text=f"Имя: {user_data['person_name']}\n"
                                    f"Номер телефона: {user_data['person_number']}\n"
                                    f"ID: {message.from_user.id}", chat_id=admin)
    await state.finish()
