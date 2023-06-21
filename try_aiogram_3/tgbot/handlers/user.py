from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from ..keyboards.reply import language_keyboard, languages
from ..keyboards.inline import all_func_keyboard
from ..misc.states import Language

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, state: FSMContext):
    await message.answer(text='Привет! | Hello!',
                         reply_markup=language_keyboard)
    await state.set_state(Language.choosing_language)


@user_router.message(Language.choosing_language, F.text == 'Русский 🇷🇺')
async def all_func_rus(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(text=f'{user_data}')
    await message.reply("Здесь ты можешь посмотреть функции этого бота!",
                        reply_markup=all_func_keyboard)


@user_router.message(Language.choosing_language, F.text == 'English 🇺🇸')
async def all_func_eng(message: Message, state: FSMContext):
    await message.reply("Here you can see the functions of this bot!",
                        reply_markup=all_func_keyboard)
