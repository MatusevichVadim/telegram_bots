from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_language = [
    [KeyboardButton(text='Русский 🇷🇺'),
     KeyboardButton(text='English 🇺🇸')]
]

language_keyboard = ReplyKeyboardMarkup(
    keyboard=kb_language,
    resize_keyboard=True,
    input_field_placeholder="Выберите язык | Choose language"
)
