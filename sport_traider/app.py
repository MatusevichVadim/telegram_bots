from aiogram import executor

from loader import dp
import handlers
from utils.notify_admins import on_startup_notify


async def on_startup(dp):
    # уведомление о запуске
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)


# @dp.message_handler()
# async def get_message(message: types.Message):
#     chat_id = message.chat.id
#     text = 'Text'
#     sent_message = await bot.send_message(chat_id=chat_id, text=text)
#     print(sent_message.to_python())
#


# executor.start_polling(dp)

# callback quaery для кнопок
# {
#   "ok": true,
#   "result": [
#     {
#       "update_id": 177965252,
#       "message": {
#         "message_id": 2,
#         "from": {
#           "id": 422844554,
#           "is_bot": false,
#           "first_name": "Elmo",
#           "last_name": "Eeeeee",
#           "username": "Elmooo_ya",
#           "language_code": "en"
#         },
#         "chat": {
#           "id": 422844554,
#           "first_name": "Elmo",
#           "last_name": "Eeeeee",
#           "username": "Elmooo_ya",
#           "type": "private"
#         },
#         "date": 1685278832,
#         "text": "sd"
#       }
#     }
#   ]
# }
