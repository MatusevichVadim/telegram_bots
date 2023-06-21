from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from ..keyboards.reply import language_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Привет!",
                        reply_markup=language_keyboard)


@user_router.message()
async def user_start(message: Message):
    await message.reply("Привет!",
                        reply_markup=language_keyboard)
