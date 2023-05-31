для linux
Должен быть установлен python3 (sudo apt install python3)
В папке бота python3 -m venv venv
python3 source venv/bin/activate
pip install -r requirements.txt
python3 app.py

windows
Должен быть установлен python3 (установить с сайта https://www.python.org/downloads/)
В папке бота py -m venv venv
py venv/Scripts\activate
pip install -r requirements.txt
python3 app.py

бот готов, в папке data/config admin, внести id чата админа, чтобы приходило оповещение о запуске бота
картинки лежат в папке data, загружать картинку добавлением в handlers/users/menu в переменные картинок

API для coinmarketa добавить в файл .env в поле API_KEY=################################# вместо решеток
