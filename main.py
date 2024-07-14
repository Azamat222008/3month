import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import random



load_dotenv()
bot = Bot(token=getenv("my_tg_token"))
dp = Dispatcher()

recipes = [['манты:',['мясо','тесто']],
           ['пицца',['тесто','томатная паста','колбаса','сыр']],
           ['плов',['мясо','морковь','рис']],
           ['гамбургер',['булочка','соус','котлета','салат','помидор','маринованные огурцы','сыр']],
           ['фрикасе с рисом',['рис','сливочный соус','курица','кукуруза','грибы',]]]


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name},")

@dp.message(Command("my_info"))
async def my_info(message: types.Message):
    await message.answer(f"Имя: {message.from_user.first_name}\n"
                         f"id: {message.from_user.id}\n"
                         f"Username: {message.from_user.username}")

@dp.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    random_recipee = random.choice(recipes)
    await message.answer(f'{random_recipee[0]}\n'
                         f'{random_recipee[1]}\n')




async def main():
   await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())