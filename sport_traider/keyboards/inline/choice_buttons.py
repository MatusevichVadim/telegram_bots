from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callbacks_data import choose_region_callback, \
    choose_product_callback, choose_language_callback, selected_product_callback, order_payment_callback, \
    coin_callback, selected_coin_callback, check_txid_callback

choice_language_inline = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Русский",
            callback_data=choose_language_callback.new(language="Русский")
        ),
        InlineKeyboardButton(
            text="English",
            callback_data=choose_language_callback.new(language="English")
        )
    ],
])

choice_region_inline = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Калининград",
            callback_data=choose_region_callback.new(region="Калининград")
        ),
        InlineKeyboardButton(
            text="Москва",
            callback_data=choose_region_callback.new(region="Москва")
        ),
    ],
    [
        InlineKeyboardButton(
            text="Сменить локализацию",
            callback_data=choose_region_callback.new(region="Сменить локализацию")
        ),
    ]
])
eng_choice_region_inline = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Kaliningrad",
            callback_data=choose_region_callback.new(region="Kaliningrad")
        ),
        InlineKeyboardButton(
            text="Moscow",
            callback_data=choose_region_callback.new(region="Moscow")
        ),
    ],
    [
        InlineKeyboardButton(
            text="Change localization",
            callback_data=choose_region_callback.new(region="Change localization")
        ),
    ]
])

choice_product_inline = InlineKeyboardMarkup(row_width=5, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Тестостерон",
            callback_data=choose_product_callback.new(item_name="Тестостерон")
        ),
    ], [
        InlineKeyboardButton(
            text="Метандростенолон",
            callback_data=choose_product_callback.new(item_name="Метандростенолон")
        ),
    ], [
        InlineKeyboardButton(
            text="Стромбафорт",
            callback_data=choose_product_callback.new(item_name="Стромбафорт")
        ),
    ], [
        InlineKeyboardButton(
            text="Сменить город",
            callback_data=choose_product_callback.new(item_name="Сменить город")
        ),
    ], [
        InlineKeyboardButton(
            text="Активные оплаты",
            callback_data=choose_product_callback.new(item_name="Активные оплаты")
        ),
    ]
])
eng_choice_product_inline = InlineKeyboardMarkup(row_width=5, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Testosterone",
            callback_data=choose_product_callback.new(item_name="Testosterone")
        ),
    ], [
        InlineKeyboardButton(
            text="Methandrostenolone",
            callback_data=choose_product_callback.new(item_name="Methandrostenolone")
        ),
    ], [
        InlineKeyboardButton(
            text="Strombafort",
            callback_data=choose_product_callback.new(item_name="Strombafort")
        ),
    ], [
        InlineKeyboardButton(
            text="Change City",
            callback_data=choose_product_callback.new(item_name="Change City")
        ),
    ], [
        InlineKeyboardButton(
            text="Active Payments",
            callback_data=choose_product_callback.new(item_name="Active Payments")
        ),
    ]
])

choice_testosterone_inline = InlineKeyboardMarkup(row_width=7, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Тестостерон Балканы 10 амп. 40$",
            callback_data=selected_product_callback.new(item_name="Тестостерон Балканы",
                                                        quantity="10 амп.",
                                                        price="40$")
        ),
    ], [
        InlineKeyboardButton(
            text="Тестостерон Балканы 30 апм. 115$",
            callback_data=selected_product_callback.new(item_name="Тестостерон Балканы",
                                                        quantity="30 амп.",
                                                        price="115$")
        ),
    ], [
        InlineKeyboardButton(
            text="Тестостерон Балканы 50 амп. 185$",
            callback_data=selected_product_callback.new(item_name="Тестостерон Балканы",
                                                        quantity="30 амп.",
                                                        price="185$")
        ),
    ], [
        InlineKeyboardButton(
            text="Тестостерон Франция 10 амп. 40$",
            callback_data=selected_product_callback.new(item_name="Тестостерон Франция",
                                                        quantity="10 амп.",
                                                        price="40$")
        ),
    ], [
        InlineKeyboardButton(
            text="Тестостерон Франция 30 амп. 115$",
            callback_data=selected_product_callback.new(item_name="Тестостерон Франция",
                                                        quantity="30 амп.",
                                                        price="115$")
        ),
    ], [
        InlineKeyboardButton(
            text="Тестостерон Франция 50 амп. 185$",
            callback_data=selected_product_callback.new(item_name="Тестостерон Франция",
                                                        quantity="50 амп.",
                                                        price="185$")
        ),
    ], [
        InlineKeyboardButton(
            text="Назад",
            callback_data=selected_product_callback.new(item_name="Назад",
                                                        quantity="",
                                                        price="")
        ),
    ]
])
eng_choice_testosterone_inline = InlineKeyboardMarkup(row_width=7, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Testosterone Balkans 10 amp. 40$",
            callback_data=selected_product_callback.new(item_name="Testosterone Balkans",
                                                        quantity="10 amp.",
                                                        price="40$")
        ),
    ], [
        InlineKeyboardButton(
            text="Testosterone Balkans 30 amp. 115$",
            callback_data=selected_product_callback.new(item_name="Testosterone Balkans",
                                                        quantity="30 amp.",
                                                        price="115$")
        ),
    ], [
        InlineKeyboardButton(
            text="Testosterone Balkans 50 amp. 185$",
            callback_data=selected_product_callback.new(item_name="Testosterone Balkans",
                                                        quantity="30 amp.",
                                                        price="185$")
        ),
    ], [
        InlineKeyboardButton(
            text="Testosterone France 10 amp. 40$",
            callback_data=selected_product_callback.new(item_name="Testosterone France",
                                                        quantity="10 amp.",
                                                        price="40$")
        ),
    ], [
        InlineKeyboardButton(
            text="Testosterone France 30 амп. 115$",
            callback_data=selected_product_callback.new(item_name="Testosterone France",
                                                        quantity="30 amp.",
                                                        price="115$")
        ),
    ], [
        InlineKeyboardButton(
            text="Testosterone France 50 амп. 185$",
            callback_data=selected_product_callback.new(item_name="Testosterone France",
                                                        quantity="50 amp.",
                                                        price="185$")
        ),
    ], [
        InlineKeyboardButton(
            text="Back",
            callback_data=selected_product_callback.new(item_name="Back",
                                                        quantity="",
                                                        price="")
        ),
    ]
])

choice_methandrostenolone_inline = InlineKeyboardMarkup(row_width=5, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="2 упак Метандростенолон-10 170 mg. 78$",
            callback_data=selected_product_callback.new(item_name="Метандростенолон",
                                                        quantity="2 упак",
                                                        price="78$")
        ),
    ], [
        InlineKeyboardButton(
            text="3 упак Метандростенолон-10 170 mg. 108$",
            callback_data=selected_product_callback.new(item_name="Метандростенолон",
                                                        quantity="3 упак",
                                                        price="108$")
        ),
    ], [
        InlineKeyboardButton(
            text="5 упак Метандростенолон-10 170 mg. 170$",
            callback_data=selected_product_callback.new(item_name="Метандростенолон",
                                                        quantity="5 упак",
                                                        price="170$")
        ),
    ], [
        InlineKeyboardButton(
            text="10 упак Метандростенолон-10 170 mg. 380$",
            callback_data=selected_product_callback.new(item_name="Метандростенолон",
                                                        quantity="10 упак",
                                                        price="380$")
        ),
    ], [
        InlineKeyboardButton(
            text="Назад",
            callback_data=selected_product_callback.new(item_name="Назад",
                                                        quantity="",
                                                        price="")
        ),
    ]
])
eng_choice_methandrostenolone_inline = InlineKeyboardMarkup(row_width=5, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="2 pack Methandrostenolone-10 170 mg. 78$",
            callback_data=selected_product_callback.new(item_name="Methandrostenolone",
                                                        quantity="2 pack",
                                                        price="78$")
        ),
    ], [
        InlineKeyboardButton(
            text="3 pack Methandrostenolone-10 170 mg. 108$",
            callback_data=selected_product_callback.new(item_name="Methandrostenolone",
                                                        quantity="3 pack",
                                                        price="108$")
        ),
    ], [
        InlineKeyboardButton(
            text="5 pack Methandrostenolone-10 170 mg. 170$",
            callback_data=selected_product_callback.new(item_name="Methandrostenolone",
                                                        quantity="5 pack",
                                                        price="170$")
        ),
    ], [
        InlineKeyboardButton(
            text="10 pack Methandrostenolone-10 170 mg. 380$",
            callback_data=selected_product_callback.new(item_name="Methandrostenolone",
                                                        quantity="10 pack",
                                                        price="380$")
        ),
    ], [
        InlineKeyboardButton(
            text="Back",
            callback_data=selected_product_callback.new(item_name="Back",
                                                        quantity="",
                                                        price="")
        ),
    ]
])

choice_strombafort_inline = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Стромбафорт 6 упак. 117$",
            callback_data=selected_product_callback.new(item_name="Стромбафорт",
                                                        quantity="6 упак",
                                                        price="117$")
        ),
    ], [
        InlineKeyboardButton(
            text="Стромбафорт 15 упак. 238$",
            callback_data=selected_product_callback.new(item_name="Стромбафорт",
                                                        quantity="15 упак",
                                                        price="238$")
        ),
    ], [
        InlineKeyboardButton(
            text="Назад",
            callback_data=selected_product_callback.new(item_name="Назад",
                                                        quantity="",
                                                        price="")
        ),
    ]
])
eng_choice_strombafort_inline = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Strombafort 6 pack. 117$",
            callback_data=selected_product_callback.new(item_name="Strombafort",
                                                        quantity="6 pack",
                                                        price="117$")
        ),
    ], [
        InlineKeyboardButton(
            text="Strombafort 15 pack. 238$",
            callback_data=selected_product_callback.new(item_name="Strombafort",
                                                        quantity="15 pack",
                                                        price="238$")
        ),
    ], [
        InlineKeyboardButton(
            text="Back",
            callback_data=selected_product_callback.new(item_name="back",
                                                        quantity="",
                                                        price="")
        ),
    ]
])

order_payment_inline = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Оплатить",
            callback_data=order_payment_callback.new(command="Оплатить")
        )], [
        InlineKeyboardButton(
            text="Назад",
            callback_data=order_payment_callback.new(command="Назад")
        )
    ]
])
eng_order_payment_inline = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Pay",
            callback_data=order_payment_callback.new(command="Pay")
        )], [
        InlineKeyboardButton(
            text="Back",
            callback_data=order_payment_callback.new(command="Back")
        )
    ]
])

coin_inline = InlineKeyboardMarkup(row_width=6, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="BTC",
            callback_data=coin_callback.new(coin="BTC", language="RU")
        )], [
        InlineKeyboardButton(
            text="ETH",
            callback_data=coin_callback.new(coin="ETH", language="RU")
        )], [
        InlineKeyboardButton(
            text="USDT trc20",
            callback_data=coin_callback.new(coin="USDT trc20", language="RU")
        )], [
        InlineKeyboardButton(
            text="XMR",
            callback_data=coin_callback.new(coin="XMR", language="RU")
        )], [
        InlineKeyboardButton(
            text="ZEC",
            callback_data=coin_callback.new(coin="ZEC", language="RU")
        )], [
        InlineKeyboardButton(
            text="LTC",
            callback_data=coin_callback.new(coin="LTC", language="RU")
        )], [
        InlineKeyboardButton(
            text="Назад",
            callback_data=coin_callback.new(coin="Назад", language="RU")
        )],
])
eng_coin_inline = InlineKeyboardMarkup(row_width=6, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="BTC",
            callback_data=coin_callback.new(coin="BTC", language="ENG")
        )], [
        InlineKeyboardButton(
            text="ETH",
            callback_data=coin_callback.new(coin="ETH", language="ENG")
        )], [
        InlineKeyboardButton(
            text="USDT trc20",
            callback_data=coin_callback.new(coin="USDT trc20", language="ENG")
        )], [
        InlineKeyboardButton(
            text="XMR",
            callback_data=coin_callback.new(coin="XMR", language="ENG")
        )], [
        InlineKeyboardButton(
            text="ZEC",
            callback_data=coin_callback.new(coin="ZEC", language="ENG")
        )], [
        InlineKeyboardButton(
            text="LTC",
            callback_data=coin_callback.new(coin="LTC", language="ENG")
        )], [
        InlineKeyboardButton(
            text="Back",
            callback_data=coin_callback.new(coin="Back", language="ENG")
        )],
])

selected_coin_inline = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Отменить оплату",
            callback_data=selected_coin_callback.new(action="Отменить оплату")
        )]
])
eng_selected_coin_inline = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Cancel payment",
            callback_data=selected_coin_callback.new(action="Cancel payment")
        )]
])

check_txid_inline = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data=check_txid_callback.new(action="Назад")
        )]
])
eng_check_txid_inline = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Back",
            callback_data=check_txid_callback.new(action="Back")
        )]
])
