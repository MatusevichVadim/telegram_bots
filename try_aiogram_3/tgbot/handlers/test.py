import random
from aiogram import types, Router, F
from aiogram.filters import StateFilter, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

test_router = Router()

stickers_list = [
    "CAACAgIAAxkBAAEJRcdkhIWGql-zco1U4ji1MI4DTSWJjwACCwADPeGrF5DVuSuO0KL7LwQ",
    "CAACAgIAAxkBAAEJRclkhIWrpBXV6NEahX4VylgkXgV7IQACpwADOlyjF7xq8d-I-KhsLwQ",
    "CAACAgIAAxkBAAEJRctkhIXYxm1_7GmWogdRxC_8NFI98wACewADOlyjF7x7qfMVfF-BLwQ"
]
HELP_COMMAND = """
/start - <b>HEEELLLLLLLLO</b>
/help - <code>123123123</code>
/stik - <code>123123123</code>
/inlinekeyboard - <code>123123123</code>
/test - <code>123123123</code>
"""

keyboard = [
    [KeyboardButton(text='/help')]
]
kb = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


@test_router.message(CommandStart(), StateFilter(None))
async def start_handler(message: types.Message) -> None:
    await message.answer(text='All command',
                         reply_markup=kb)


@test_router.message(F.text == 'help', StateFilter(None))
async def help_handler(message: types.Message) -> None:
    await message.reply(text=HELP_COMMAND,
                        reply_markup=ReplyKeyboardRemove())


@test_router.message(F.text == 'stik', StateFilter(None))
async def stik_handler(message: types.Message) -> None:
    await message.answer_sticker(random.choice(stickers_list))
    await message.delete()


keyboard = [
    [InlineKeyboardButton(text='1', callback_data='1')],
    [InlineKeyboardButton(text='2', callback_data='2')],
    []
]

ikb = InlineKeyboardMarkup(inline_keyboard=keyboard, row_width=2)

keyboard_2 = [
    [InlineKeyboardButton(text='Rus', callback_data='Rus'),
     InlineKeyboardButton(text='Eng', callback_data='Eng')
     ],
]

inline_language = InlineKeyboardMarkup(inline_keyboard=keyboard_2, row_width=1)


@test_router.message(F.text == 'inlinekeyboard', StateFilter(None))
async def inline_handler(message: types.Message) -> None:
    await message.answer(text='1',
                         reply_markup=ikb)


@test_router.message(F.text)
async def handler(message: types.Message) -> None:
    await message.answer(text='/start')
