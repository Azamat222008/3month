from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters.command import Command


my_info_router = Router()


@my_info_router.message(Command("my_info"))
async def my_info(message: types.Message):
    await message.answer(f"Имя: {message.from_user.first_name}\n"
                         f"id: {message.from_user.id}\n"
                         f"Username: {message.from_user.username}")