#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25261856"))
API_HASH = environ.get("API_HASH", "c61d8597c11edf9ab583a2966b94d330")
BOT_TOKEN = environ.get("BOT_TOKEN", "8132042900:AAEmllEmnKRoi_VdrOlfjr3ov6-SZNoLBzs")

OWNER = int(environ.get("OWNER", "6053889491"))
CREDIT = environ.get("CREDIT", "kumawat_bots")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6053889491').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6053889491').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
