import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))
API_KEY = str(os.getenv("API_KEY"))
admins = []

ip = os.getenv("ip")

aiogram_redis = {
    "host": ip,
}

redis = {
    "address": (ip, 6379),
    "encoding": "utf8"
}
