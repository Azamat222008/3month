from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters.command import Command
import random
from aiogram.types import FSInputFile

dishes_router = Router()

@dishes_router.message(F.text == 'Холодные напитки')
async def drinks(message: types.Message):
    photo = FSInputFile('images/Coca-Cola.png')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption='Coca-Cola'
    )