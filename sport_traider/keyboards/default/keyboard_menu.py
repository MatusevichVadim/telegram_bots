from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Русский"),
            KeyboardButton(text="English"),

        ]
    ],
    resize_keyboard=True
)

# city = ReplyKeyboardMarkup(
#     [
#         [
#             KeyboardButton(text="Калининград"),
#             KeyboardButton(text="Москва"),
#         ],
#         [
#             KeyboardButton(text="Сменить локализацию"),
#         ]
#     ],
#     resize_keyboard=True
# )
