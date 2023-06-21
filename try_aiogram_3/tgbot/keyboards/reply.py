from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

languages = [
    'Русский 🇷🇺',
    'English 🇺🇸'
]

kb_language = [
    [KeyboardButton(text=i) for i in languages]
]

language_keyboard = ReplyKeyboardMarkup(
    keyboard=kb_language,
    resize_keyboard=True,
    input_field_placeholder="Выберите язык | Choose language"
)
