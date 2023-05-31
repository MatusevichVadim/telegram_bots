from aiogram.utils.callback_data import CallbackData

choose_language_callback = CallbackData("choice", "language")
choose_region_callback = CallbackData("choice", "region")
choose_product_callback = CallbackData("choice", "item_name")
selected_product_callback = CallbackData("select", "item_name", "quantity", "price")
order_payment_callback = CallbackData("order_payment", "command")
coin_callback = CallbackData("payment", "coin", "language")
selected_coin_callback = CallbackData("payment", "action")
check_txid_callback = CallbackData("payment", "action")

