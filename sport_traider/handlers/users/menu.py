import datetime
import logging

from aiogram import types
from aiogram.types import ParseMode, InputMediaPhoto
from aiogram.dispatcher.filters import CommandStart, Text

import keyboards.inline.choice_buttons as c_but
import keyboards.inline.callbacks_data as call_d
from loader import dp, bot
from utils.coinmarketcap import actual_cost

from aiogram.types import CallbackQuery

Testosterone_PHOTO = 'data/PROPANDROL.jpg'
Methandrostenolone_PHOTO = 'data/METAN.jpg'
Strombafort_PHOTO = 'data/PROPANDROL.jpg'

LOCALIZATION = "Русский"

ACTIVE_PAYMENT = {}
PAYMENT_MESSAGE = 0

price = 0
coin_dict = {'BTC': "BTC: <code>Bt7357hggjk63ffjlcszxvb53fs256gfsjjch531j</code>",
             'ETH': 'ETH: <code>Eth99357hggjk63ffjlcszxvb53fs256gffgh531j</code>',
             'USDT trc20': 'USDT trc20: <code>trc257hggjk63ffjlcszxvb53fs256gfsjjch531j</code>',
             'XMR': 'XMR: <code>XMR357hggjk63ffjlcszxvb53fs256gfsjjch531j</code>',
             'ZEC': 'ZEC: <code>LTc357hggjk63ffjlcszxvb53fs256gfsjjch531j</code>',
             'LTC': 'LTC: <code>Bt7357hggjk63ffjlcszxvb53fs256gfsjjch531j</code>'}


@dp.message_handler(CommandStart())
async def language_handler(message: types.Message):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(text="Choose your language \nВыберите язык",
                         reply_markup=c_but.choice_language_inline)


@dp.message_handler(CommandStart())
async def language_handler(message: types.Message):
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer(text="Choose your language \nВыберите язык",
                         reply_markup=c_but.choice_language_inline)


@dp.message_handler()
async def checker_txid(message: types.Message):
    if LOCALIZATION == "Русский":
        # await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await message.reply(text="Не верный TXID", reply_markup=c_but.check_txid_inline)
    else:
        # await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
        await message.reply(text="Invalid TXID", reply_markup=c_but.eng_check_txid_inline)


@dp.callback_query_handler(call_d.choose_region_callback.filter(region="Сменить локализацию"))
@dp.callback_query_handler(call_d.choose_region_callback.filter(region="Change localization"))
async def eng_change_localization(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text="Choose your language \nВыберите язык",
                              reply_markup=c_but.choice_language_inline)


@dp.callback_query_handler(call_d.choose_language_callback.filter(language="Русский"))
@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Сменить город"))
async def region_handler(call: CallbackQuery, callback_data: dict):
    global LOCALIZATION
    LOCALIZATION = callback_data.get('language')
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text=f"Качки, всех приветствую в нашем магазине. \n"
                                   f"Если будут какие нибудь вопросы, писать на @BodyBilderTest",
                              reply_markup=c_but.choice_region_inline, parse_mode=ParseMode.HTML)


@dp.callback_query_handler(call_d.choose_language_callback.filter(language="English"))
@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Change City"))
async def eng_region_handler(call: CallbackQuery, callback_data: dict):
    global LOCALIZATION
    LOCALIZATION = callback_data.get('language')
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text="Jocks, welcome to our store. \n"
                                   "If you have any questions, write to @BodyBuilderTest",
                              reply_markup=c_but.eng_choice_region_inline)


@dp.callback_query_handler(call_d.choose_region_callback.filter(region="Калининград"))
@dp.callback_query_handler(call_d.choose_region_callback.filter(region="Москва"))
async def region_product(call: CallbackQuery):
    # await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text="Меню выбора:",
                              reply_markup=c_but.choice_product_inline)


@dp.callback_query_handler(call_d.choose_region_callback.filter(region="Kaliningrad"))
@dp.callback_query_handler(call_d.choose_region_callback.filter(region="Moscow"))
async def eng_region_product(call: CallbackQuery):
    # await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text="Selection menu:",
                              reply_markup=c_but.eng_choice_product_inline)


@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Тестостерон"))
@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Метандростенолон"))
@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Стромбафорт"))
async def product(call: CallbackQuery, callback_data: dict):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    text = callback_data['item_name']
    inline_dict = {'Тестостерон': c_but.choice_testosterone_inline,
                   'Метандростенолон': c_but.choice_methandrostenolone_inline,
                   'Стромбафорт': c_but.choice_strombafort_inline
                   }
    await call.message.answer(text=f"{text}",
                              reply_markup=inline_dict[text])


@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Testosterone"))
@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Methandrostenolone"))
@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Strombafort"))
async def eng_product(call: CallbackQuery, callback_data: dict):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    text = callback_data['item_name']
    inline_dict = {'Testosterone': c_but.eng_choice_testosterone_inline,
                   'Methandrostenolone': c_but.eng_choice_methandrostenolone_inline,
                   'Strombafort': c_but.eng_choice_strombafort_inline
                   }
    await call.message.answer(text=f"{text}", reply_markup=inline_dict[text])


@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Активные оплаты"))
async def send_payment_alert(call: CallbackQuery, callback_data: dict):
    text = ''
    now = datetime.datetime.now()
    NONEACTIVE_PAYMENT = []
    for key, value in ACTIVE_PAYMENT.items():
        print(f"{int(now.hour) = } {int(key.split(':')[0]) = } {int(now.minute) + 1 = } {int(key.split(':')[1]) = }")
        if int(now.hour) + 1 > int(key.split(':')[0]) and int(now.minute) >= int(key.split(':')[1]):
            NONEACTIVE_PAYMENT.append(key)
    [ACTIVE_PAYMENT.pop(i) for i in NONEACTIVE_PAYMENT]
    if ACTIVE_PAYMENT:
        text = 'Активные оплаты:'
        for i in ACTIVE_PAYMENT.values():
            text += f"\n{str(*i)}"
    else:
        await call.answer(text="Никакой оплаты выбрано не было.", show_alert=True)
    text += '\nМеню выбора:'
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text=text, reply_markup=c_but.choice_product_inline)


@dp.callback_query_handler(call_d.choose_product_callback.filter(item_name="Active Payments"))
async def eng_send_payment_alert(call: CallbackQuery, callback_data: dict):
    text = ''
    now = datetime.datetime.now()
    NONEACTIVE_PAYMENT = []
    for key, value in ACTIVE_PAYMENT.items():
        print(f"{int(now.hour) = } {int(key.split(':')[0]) = } {int(now.minute) + 1 = } {int(key.split(':')[1]) = }")
        if int(now.hour) >= int(key.split(':')[0]) and int(now.minute) + 1 > int(key.split(':')[1]):
            NONEACTIVE_PAYMENT.append(key)
    [ACTIVE_PAYMENT.pop(i) for i in NONEACTIVE_PAYMENT]
    if ACTIVE_PAYMENT:
        text = 'Active Payments:'
        for i in ACTIVE_PAYMENT.values():
            text += f"\n{str(*i)}"
    else:
        await call.answer(text="No payment was selected.", show_alert=True)
    text += '\nSelection menu:'
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text=text, reply_markup=c_but.eng_choice_product_inline)


@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Тестостерон Балканы"))
@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Тестостерон Франция"))
@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Метандростенолон"))
@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Стромбафорт"))
async def choise_testosterone_product(call: CallbackQuery, callback_data: dict):
    global price
    price = int(callback_data["price"][:-1])
    chat_id = call.message.chat.id
    inline_choose = callback_data['item_name'].split(' ')[0]
    inline_dict = {'Тестостерон': c_but.order_payment_inline,
                   'Метандростенолон': c_but.order_payment_inline,
                   'Стромбафорт': c_but.order_payment_inline
                   }
    company = {'Тестостерон': 'Balkan Pharmaceuticals',
               'Метандростенолон': 'Balkan Pharmaceuticals Danabol',
               'Стромбафорт': 'Strombafort'
               }
    basis = {'Тестостерон': "Тестостерон 10 мл\nП/НП 60% / 40%\n%: 10-11%",
             'Метандростенолон': "Метандростенолон 10мг.\nП/НП 11% / 3%\n%: 4-6%",
             'Стромбафорт': "Станозолол 10мг.\nП/НП 7% / 9%\n%: 12-16%"}
    countries = ['Молдова', 'Франция']
    photos = {'Тестостерон': Testosterone_PHOTO,
              'Метандростенолон': Methandrostenolone_PHOTO,
              'Стромбафорт': Strombafort_PHOTO}
    if 'Франция' in callback_data.get('item_name'):
        country = countries[1]
    else:
        country = countries[0]
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.send_photo(chat_id=chat_id, photo=open(photos[inline_choose], 'rb'),
                         caption=f"{company[inline_choose]} \n"
                                 f"Страна {country}\n" + basis[inline_choose],
                         reply_markup=inline_dict[inline_choose])


@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Testosterone Balkans"))
@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Testosterone France"))
@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Methandrostenolone"))
@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Strombafort"))
async def eng_choise_testosterone_product(call: CallbackQuery, callback_data: dict):
    global price
    price = int(callback_data["price"][:-1])
    chat_id = call.message.chat.id
    inline_choose = callback_data['item_name'].split(' ')[0]
    inline_dict = {'Testosterone': c_but.eng_order_payment_inline,
                   'Methandrostenolone': c_but.eng_order_payment_inline,
                   'Strombafort': c_but.eng_order_payment_inline
                   }
    company = {'Testosterone': 'Balkan Pharmaceuticals',
               'Methandrostenolone': 'Balkan Pharmaceuticals Danabol',
               'Strombafort': 'Strombafort'
               }
    basis = {'Testosterone': "Testosterone 10ml\nP/NP 60% / 40%\n%: 10-11%",
             'Methandrostenolone': "Metandrostenolone 10mg.\nP/NP 11% / 3%\n%: 4-6%",
             'Strombafort': "Stanozolol 10mg.\nP/NP 7% / 9%\n%: 12-16%"}
    photos = {'Testosterone': Testosterone_PHOTO,
              'Methandrostenolone': Methandrostenolone_PHOTO,
              'Strombafort': Strombafort_PHOTO}
    countries = ['Moldova', 'France']
    if 'France' in callback_data.get('item_name'):
        country = countries[1]
    else:
        country = countries[0]
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.send_photo(chat_id=chat_id, photo=open(photos[inline_choose], 'rb'),
                         caption=f"{company[inline_choose]} \n"
                                 f"Country {country}\n" + basis[inline_choose],
                         reply_markup=inline_dict[inline_choose])


@dp.callback_query_handler(call_d.order_payment_callback.filter(command="Оплатить"))
@dp.callback_query_handler(call_d.check_txid_callback.filter(action="Назад"))
async def order_payment(call: CallbackQuery, callback_data: dict):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text='Доступные виды отплаты:', reply_markup=c_but.coin_inline)


@dp.callback_query_handler(call_d.order_payment_callback.filter(command="Pay"))
@dp.callback_query_handler(call_d.check_txid_callback.filter(action="Back"))
async def eng_order_payment(call: CallbackQuery, callback_data: dict):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text='Available payment types:', reply_markup=c_but.eng_coin_inline)


@dp.callback_query_handler(call_d.coin_callback.filter(coin="BTC"))
@dp.callback_query_handler(call_d.coin_callback.filter(coin="ETH"))
@dp.callback_query_handler(call_d.coin_callback.filter(coin="USDT trc20"))
@dp.callback_query_handler(call_d.coin_callback.filter(coin="XMR"))
@dp.callback_query_handler(call_d.coin_callback.filter(coin="ZEC"))
@dp.callback_query_handler(call_d.coin_callback.filter(coin="LTC"))
async def send_payment_alert(call: CallbackQuery, callback_data: dict):
    global ACTIVE_PAYMENT
    language = callback_data['language']
    if language == "RU":
        inline = c_but.selected_coin_inline
        TXID = "После оплаты прислать TXID транзакции."
        pay_before_text = 'Оплатить до:'
    else:
        inline = c_but.eng_selected_coin_inline
        TXID = "Send TXID of transaction after payment."
        pay_before_text = 'Pay up to:'
    coin = callback_data.get('coin')
    pay_before = datetime.datetime.now() + datetime.timedelta(hours=1)
    actual_cost_date = actual_cost[coin][1].split('T')
    text = f"{coin_dict[coin]}\n" \
           f"{price}$ = <code>{round(price / actual_cost[coin][0], 5)}</code> {coin}\n" \
           f"{pay_before_text} {pay_before.hour}:{pay_before.minute} \n" \
           f"{TXID}"
    ACTIVE_PAYMENT[f'{pay_before.hour}:{pay_before.minute}'] = [text]

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text=text, reply_markup=inline, parse_mode='HTML')


@dp.callback_query_handler(call_d.selected_coin_callback.filter(action="Отменить оплату"))
async def send_payment_alert(call: CallbackQuery, callback_data: dict):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    global PAYMENT_MESSAGE
    PAYMENT_MESSAGE = call.message.message_id
    try:
        ACTIVE_PAYMENT.popitem()
    except IndexError:
        await call.answer(text="Никакой оплаты выбрано не было.", show_alert=True)
    await call.message.answer(text='Доступные виды отплаты:', reply_markup=c_but.coin_inline)


@dp.callback_query_handler(call_d.selected_coin_callback.filter(action="Cancel payment"))
async def eng_send_payment_alert(call: CallbackQuery, callback_data: dict):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    global PAYMENT_MESSAGE
    PAYMENT_MESSAGE = call.message.message_id
    try:
        ACTIVE_PAYMENT.popitem()
    except IndexError:
        await call.answer(text="Никакой оплаты выбрано не было.", show_alert=True)
    await call.message.answer(text='Available payment types:', reply_markup=c_but.eng_coin_inline)


@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Назад"))
@dp.callback_query_handler(call_d.order_payment_callback.filter(command="Назад"))
@dp.callback_query_handler(call_d.coin_callback.filter(coin="Назад"))
async def back_to_choose_product(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text="Меню выбора:",
                              reply_markup=c_but.choice_product_inline)


@dp.callback_query_handler(call_d.selected_product_callback.filter(item_name="Back"))
@dp.callback_query_handler(call_d.order_payment_callback.filter(command="Back"))
@dp.callback_query_handler(call_d.coin_callback.filter(coin="Back"))
async def eng_back_to_choose_product(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(text="Selection menu:",
                              reply_markup=c_but.eng_choice_product_inline)
