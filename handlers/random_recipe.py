from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters.command import Command
import random


recipe_router = Router()



recipes = [['манты:',['мясо','тесто']],
           ['пицца',['тесто','томатная паста','колбаса','сыр']],
           ['плов',['мясо','морковь','рис']],
           ['гамбургер',['булочка','соус','котлета','салат','помидор','маринованные огурцы','сыр']],
           ['фрикасе с рисом',['рис','сливочный соус','курица','кукуруза','грибы',]]]




@recipe_router.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    random_recipee = random.choice(recipes)
    await message.answer(f'{random_recipee[0]}\n'
                         f'{random_recipee[1]}\n')