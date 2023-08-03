import datetime
import time

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.tl.functions.messages import GetHistoryRequest
from multiprocessing import Process
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import asyncio
import random
import json
import socks

import sessions

red = "\033[1;31m"
green = "\033[1;32m"
blue = "\033[1;36m"

with open('config.json', 'r') as config:
    all_date = json.load(config)
delay = int(all_date['delay'])
thread = int(all_date['threading'])
random_work_time = list(range(all_date['random_time'][0], all_date['random_time'][1]))

loop = asyncio.new_event_loop()
scheduler = AsyncIOScheduler()


async def sleeping_time():
    my_time = datetime.datetime.now() + datetime.timedelta(minutes=random.choice(random_work_time))
    # my_time = random.choice(random_work_time)
    print(f'We are in sleeping_time {my_time.time().minute = }')
    await asyncio.sleep(my_time.time().minute)


async def get_messages_from_channel(client, chat_id, session=None):
    all_messages = []
    # channel_for_messaging = int(all_date['channel_for_messaging'])
    channel_for_messaging = all_date['all_sessions'][0][session]['channel_for_messaging']
    print(f'{channel_for_messaging = }')
    channel_entity = await client.get_entity(channel_for_messaging)
    # await sleeping_time()
    history = await client(GetHistoryRequest(
        peer=channel_entity,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))
    for message in history.messages:
        try:
            all_messages.append(message.to_dict()['message'])
        except KeyError:
            continue
    random_message = random.choice(all_messages)
    message_time = str(datetime.datetime.now() +
                       datetime.timedelta(minutes=random.choice(random_work_time)))[:-7]
    print(green + f'Для сессии {session} cозданно сообщение: "{random_message}" '
                  f'оно будет отправленно в {message_time} в чат: {chat_id}')
    try:
        scheduler.add_job(
            send_message_to_group,
            'date',
            run_date=message_time,
            args=(client, chat_id, random_message)
        )
        if not scheduler.running:
            scheduler.start()
    except BaseException as er:
        print(f'Ошибка {scheduler = } and {er = }')
    # await send_message_to_group(client, chat_id, random_message)


async def send_message_to_group(client, group_id, message):
    try:
        # print(re + f"[!] ждем {delay}c")
        # await asyncio.sleep(delay)

        await client.send_message(group_id, message)
        # print(re + f"Создали таск в send_message_to_group {group_id = }, {message = } ")
        # print(f"Cоздан вызов в {group_id = }, c {message = } ")
        # await client.loop.call_later(delay, send_message_to_group, client, group_id, message)
    except RuntimeWarning as er:
        print(red + f"[!] Словили {er}\n")
    except PeerFloodError:
        print(red + "[!] Получил предупреждение о спаме от Телеграма. \n"
                    "[!] Эта сессия остановлена. \n"
                    "[!] Переходим к следующей.")

        client.disconnect()
        # sys.exit()


def seq_chats(client, session):
    tasks = []
    for chat_id in all_date['all_sessions'][0][session]['chats']:
        # print(green + f'{session = } ', end='')
        tasks.append(loop.create_task(get_messages_from_channel(client, chat_id, session)))
        # try:
        #     message = random.choice(all_date['all_sessions'][0][session]['message'])
        #     print(gr + f'{session = } ', end='')
        #     # print(f'из seq_chats {message = }, {session = }')
        #     # client.loop.run_until_complete(client.loop.create_task(client.send_message(chat_id, message)))
        #     client.loop.create_task(send_message_to_group(client, chat_id))
        # except IndexError:
        #     print(re + f"[!] Добавьте сообщение в {session} \n")
        #
    try:
        client.loop.run_until_complete(asyncio.gather(*tasks))
        # client.loop.run_until_complete(get_messages_from_channel(client, chat_id))
    except IndexError:
        print(red + f"[!] Добавьте сообщение в {session} \n")


def main():
    asyncio.set_event_loop(loop)

    for session, value in all_date['all_sessions'][0].items():
        if all_date['all_sessions'][0][session]['proxies']:
            for proxy in all_date['all_sessions'][0][session]['proxies']:
                ip, port, login, password = proxy.split(':')
                try:
                    client = TelegramClient(session,
                                            value['api_id'],
                                            value['api_hash'],
                                            proxy=(socks.SOCKS5, ip, int(port), login, password))
                    client.start()
                    # th = Thread(target=seq_chats, args=(client, session))
                    # th.start()
                    seq_chats(client, session)
                except:
                    print(red + "[!] Что-то пошло не так, переходим к следующей сессии. \n")
        else:
            try:
                client = TelegramClient(session, value['api_id'], value['api_hash'])
                client.start()
                # a = Process(target=seq_chats, args=(client, session), daemon=True)
                # a.start()
                # a.join()
                seq_chats(client, session)
            except:
                print(red + "[!] Что-то пошло не так, переходим к следующей сессии. \n")
    else:
        print(f'Все задачи созданы. Мы ушли в цикл задач. Количество задач : {len(scheduler.get_jobs())}')
        print(f'{scheduler.print_jobs() = }')
        while len(scheduler.get_jobs()):
            loop.run_until_complete(asyncio.sleep(1))
        print(red + "[!] Все сессии отработали, сейчас перейдем на главную. \n")
        time.sleep(5)
        sessions.main()


if __name__ == '__main__':
    main()
