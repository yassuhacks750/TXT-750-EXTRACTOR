import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22849789"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "0fc127c6055acd59f00ec6c229e1e3c4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "7296271316"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://yassuthakur750:Yash2835P@txt.qz9t8qs.mongodb.net/?retryWrites=true&w=majority&appName=Txt")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002477114210"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002477114210")  # Optional here you'll get all logs
