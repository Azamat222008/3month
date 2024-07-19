
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from database.database import Database


load_dotenv()


bot = Bot(token=getenv("my_tg_token"))
dp = Dispatcher()
db = Database('restaurant.sqlite3')