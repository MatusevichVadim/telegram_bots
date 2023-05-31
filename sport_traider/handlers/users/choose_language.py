from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command

from states import Language


@dp.message_handlers(Command('language'))
async def enter_language(message: types.Message):
    await Language.Q1.set()

# @dp.message_handlers(state=Language.Q1)
# async def asnwer
