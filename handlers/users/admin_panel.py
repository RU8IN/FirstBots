import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton

from data.config import admins
from loader import dp, bot
from states import AdminStates
from utils.misc import rate_limit

two_up = os.path.abspath(os.path.join(__file__, "../../.."))
path = two_up + '\\photos'

files = os.listdir(path)
files = [os.path.join(path, file) for file in files]
files = [file for file in files if os.path.isfile(file)]

main_message = ''


@rate_limit(5, 'send_news')
@dp.message_handler(commands="send_news", state="*")
async def send_mails(message: types.Message):
    if message.from_user.id in admins:
        await message.answer(text="Отправьте мне сообщение для рассылки")
    await AdminStates.send_news.send_news_waiting_for_message.set()


@dp.message_handler(state=AdminStates.send_news.send_news_waiting_for_message)
async def waiting_for_message(message: types.Message):
    global main_message
    buttons = [
        InlineKeyboardButton(text="Да", callback_data="yes"),
        InlineKeyboardButton(text="Нет", callback_data="no")
    ]
    keyboard = types.InlineKeyboardMarkup()
    for button in buttons:
        keyboard.add(button)
    main_message = message.text
    await message.answer(text="Требуется ли фото?", reply_markup=keyboard)
    await AdminStates.send_news.send_news_waiting_for_answer.set()


# @dp.callback_query_handler(text_contains="yes", state=AdminStates.send_news.send_news_waiting_for_answer)
# async def contains_yes(callback: types.CallbackQuery):
#     # print('dada')
#     await callback.answer(cache_time=60)
#     await bot.send_message(chat_id=callback.from_user.id, text="Пришлите фото")
#     await AdminStates.send_news.send_news_waiting_for_photo.set()


@dp.message_handler(state=AdminStates.send_news.send_news_waiting_for_photo, content_types=types.ContentTypes.PHOTO)
async def catching_photo(message: types.Message):
    await message.photo[-1].download()
    await message.answer('Фото скачано')
    await AdminStates.send_news.send_news_final.set()


@dp.callback_query_handler(text_contains="no", state=AdminStates.send_news.send_news_waiting_for_answer)
async def contains_yes(callback: types.CallbackQuery, state: FSMContext):
    global two_up
    global files
    # print('dada')
    await callback.answer(cache_time=60)
    for id in open(two_up + '/data/users_ids.txt').readlines():
        print(id)
        try:
            await bot.send_message(text=main_message, reply_markup=None, chat_id=id)
        except:
            pass
    await AdminStates.send_news.send_news_waiting_for_photo.set()
    await state.finish()


# @dp.message_handler(content_types=types.ContentTypes.TEXT, state=AdminStates.send_news.send_news_final)
# async def contains_yes(message: types.Message):
#     global two_up
#     global files
#     # print('dada')
#     print('dada')
#     for id in open(two_up + '/data/users_ids.txt').readlines():
#         print(id)
#         await bot.send_photo(photo=str(max(files, key=os.path.getctime)), chat_id=id)
#         try:
#             await bot.send_message(text=main_message, reply_markup=None, chat_id=id)
#
#             print(max(files, key=os.path.getctime))
#         except:
#             pass
#     await AdminStates.send_news.send_news_waiting_for_photo.set()
