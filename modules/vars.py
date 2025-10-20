#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27019361"))
API_HASH = environ.get("API_HASH", "b75e05daee8ff985a85778dc203dbe30")
BOT_TOKEN = environ.get("BOT_TOKEN", "8296799807:AAE9qYjdvXpXYnJ3F4G_Ua7r-5Twb3Y5Zps")

OWNER = int(environ.get("OWNER", "7306229091"))
CREDIT = environ.get("CREDIT", "kumawat_bots")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7306229091').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7306229091').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
