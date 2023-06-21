from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inlkb_all_func = [
    [
        InlineKeyboardButton(text='1',
                             callback_data='1'),
        InlineKeyboardButton(text='2',
                             callback_data='2')
    ]
]

all_func_keyboard = InlineKeyboardMarkup(inline_keyboard=inlkb_all_func)
