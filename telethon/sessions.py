from telethon import TelegramClient
from telethon.errors.rpcerrorlist import SessionPasswordNeededError
import os
import time
import sys
import json
import asyncio
from pprint import pprint
import script

red = "\033[1;31m"
green = "\033[1;32m"
blue = "\033[1;36m"
SLEEP_TIME = 30
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def banner():
    print(f"""
            {blue}           ╔══╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
            {blue}           ╠══║  ║ ╚╝ ║║ ║║ ║║ ║
            {blue}created by ╚══╚═╝╩    ╩╚═╝╚═╝╚═╝
        """)


def sleep_message():
    print("Все ок! Переходим на главную ")
    time.sleep(1)


def start_window():
    os.system('clear')
    banner()
    try:
        choice = input(green + "   [!] Выберите что вам необходимо, введя цифру\n"
                               "   [1] Создать новую сессию. \n"
                               "   [2] Изменить чаты/прокси/сообщения в существующей сессии. \n"
                               "   [3] Запустить рассылку \n"
                               "   [4] Удалить не нужную сессию (+удалить чаты и прокси сессии из config.json) \n"
                               "   [5] Выйти. \n")
    except KeyboardInterrupt:
        sys.exit(1)
    return choice


async def create_session(api_id: int, api_hash: str, phone: str, session_file: str = ''):
    client = TelegramClient(phone, api_id, api_hash, system_version="4.16.30-vxCUSTOM")
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input(green + '[+]   Введите код: ' + red))
        except SessionPasswordNeededError:
            await client.sign_in(password=input(green + '[+]   Ещё пароль: ' + red))
    return client


def get_data():
    with open('config.json', 'r') as config:
        all_date = json.load(config)
        return all_date


def set_data(all_date):
    with open('config.json', 'w+') as config:
        json_obj = json.dumps(all_date, indent=4)
        config.write(json_obj)


def add_data(objects, data):
    all_data = get_data()
    if objects == 'session':
        template = {data[0]: {
            "api_id": data[1],
            "api_hash": data[2],
            "session_file": data[0],
            "proxies": [],
            "chats": [],
        }}
        all_data['all_sessions'][0].update(template)
    elif objects == 'proxies':
        proxies = data[1].split(',')
        for proxy in proxies:
            if proxy:
                all_data['all_sessions'][0][data[0]]['proxies'].append(proxy)

    elif objects == 'chats':
        chats = data[1].split(',')
        for chat in chats:
            if chat:
                all_data['all_sessions'][0][data[0]]['chats'].append(int(chat))

    elif objects == 'message':
        all_data['channel_for_messaging'] = data[1]
    else:
        return None
    set_data(all_data)


def delete_data(phone, objects):
    all_data = get_data()
    en_data = dict()
    if objects == 'chat':
        print(green + "   [!] Выберите ненужный чат: " + red)
        for number, chat in enumerate(all_data['all_sessions'][0][phone]['chats']):
            en_data[number] = chat
            print(green + f"    [{number}] {chat}" + red)
        del_chat = int(input())
        try:
            all_data['all_sessions'][0][phone]['chats'].remove(en_data[del_chat])
        except ValueError as er:
            print(f'Странно но такой чат я удалить не могу {en_data[del_chat]}, {er}')
    elif objects == 'proxy':
        print(green + "   [!] Выберите ненужный прокси: " + red)
        for number, proxy in enumerate(all_data['all_sessions'][0][phone]['proxies']):
            en_data[number] = proxy
            print(green + f"    [{number}] {proxy}" + red)
        del_proxy = int(input())
        try:
            all_data['all_sessions'][0][phone]['proxies'].remove(en_data[del_proxy])
        except ValueError as er:
            print(f'Странно но такого прокси я удалить не могу {en_data[del_proxy]}, {er}')
    # elif objects == 'message':
    #     print(green + "   [!] Выберите ненужное сообщение: " + red)
    #     for number, message in enumerate(all_data['all_sessions'][0][phone]['message']):
    #         en_data[number] = message
    #         print(green + f"    [{number}] {message}" + red)
    #     del_message = int(input())
    #     try:
    #         all_data['all_sessions'][0][phone]['proxies'].remove(en_data[del_message])
    #     except ValueError as er:
    #         print(f'Странно но такоe сообщение я удалить не могу {en_data[del_message]}, {er}')
    set_data(all_data)
    sleep_message()
    main()


def add_proxies(phone):
    proxies = input(green + "   [!] Формат host:port:log:pass. Все прокси вводятся через запятую: " + red)
    add_data('proxies', [phone, proxies])
    sleep_message()
    main()


def add_chats(phone):
    chats = input(
        green + "   [!] Формат -1001940905060. Узнать ид чата @username_to_id_bot. Все чаты вводятся через запятую: " + red)
    add_data('chats', [phone, chats])
    sleep_message()
    main()


def add_message(phone):
    channel_for_messaging = input(green + "   [!] Формат -1001940900860. Узнать ид чата @username_to_id_bot: " + red)
    add_data('message', [phone, channel_for_messaging])
    sleep_message()
    main()


def add_sessions():
    phone = input(green + '[+]  Номер телефона (с кодом страны, например, +1231231231): ' + red)
    api_id = int(input(green + '     api_id (число): ' + red))
    api_hash = input(green + '     api_hash: ' + red)
    loop.run_until_complete(create_session(api_id=api_id, api_hash=api_hash, phone=phone))
    add_data('session', [phone, api_id, api_hash])
    print(green + '[+]  Введем прокси/чаты/сообщения?(Можно будет добавить их позже в config.json): ' + red)
    p_or_ch = input(green + "   [!] Выберите что вам необходимо, введя цифру\n"
                            "   [1] Добавить прокси. \n"
                            "   [2] Добавить чаты. \n"
                            "   [3] Добавить чат из которого будем брать сообщения. \n"
                            "   [4] Назад. \n")

    if p_or_ch == '1':
        add_proxies(phone)

    elif p_or_ch == '2':
        add_chats(phone)

    elif p_or_ch == '3':
        add_message(phone)
    else:
        main()


def change_chats_proxies_messages():
    try:
        all_date = get_data()
        print(green + "   [!] В какой сессии будем менять?" + red)
        en_date = dict()
        for number, session in enumerate(all_date['all_sessions'][0].keys()):
            en_date[number] = session
            print(green + f"    [{number}] {session}" + red)
        print(green + f"    [!] Назад" + red)
        choice_2 = input()
        if choice_2 == '!':
            main()
        else:
            os.system('clear')
            session = all_date['all_sessions'][0][en_date[int(choice_2)]]
            pprint(session)
            print(green + "   [!] Формат ввода: 11 или 22 " + red)
            print(green + "   [1] Добавим?" + red)
            print(green + "        [1] чаты." + red)
            print(green + "        [2] прокси." + red)
            print(green + "   [2] Удалим?" + red)
            print(green + "        [1] чаты." + red)
            print(green + "        [2] прокси." + red)
            print(green + "   [!] Назад" + red)
            choice_3 = input()
            if choice_3 == '11':
                add_chats(session['session_file'])
            elif choice_3 == '12':
                add_proxies(session['session_file'])
            elif choice_3 == '21':
                delete_data(session['session_file'], 'chat')
            elif choice_3 == '22':
                delete_data(session['session_file'], 'proxy')
            else:
                main()
    except KeyError:
        main()


def delete_session():
    try:
        all_date = get_data()
        print(green + "   [!] Что удалим?" + red)
        en_date = dict()
        for number, session in enumerate(all_date['all_sessions'][0].keys()):
            en_date[number] = session
            print(f"    [{number}] {session}")
        print(green + f"    [!] Назад" + red)
        choice_2 = input()
        if choice_2 == '!':
            main()
        else:
            print(all_date['all_sessions'][0][en_date[int(choice_2)]])
    except KeyError:
        main()


def main():
    choice = start_window()

    if choice == '1':
        add_sessions()

    elif choice == '2':
        change_chats_proxies_messages()

    elif choice == '3':
        script.main()

    elif choice == '4':
        delete_session()

    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
