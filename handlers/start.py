from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters.command import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
            ],
            [
                types.InlineKeyboardButton(text="Отзывы", callback_data="review"),
            ],
            [
                types.InlineKeyboardButton(text="Вакансии", callback_data="jobs"),
            ]
        ]
    )
    await message.answer("Привет",reply_markup=kb)

@start_router.callback_query(F.data =="about_us")
async def about_us(call: types.CallbackQuery):
    await call.answer("Пока ничего нет")

@start_router.callback_query(F.data =="review")
async def review(call: types.CallbackQuery):
    await call.answer("Пока ничего нет")


@start_router.callback_query(F.data =="jobs")
async def review(call: types.CallbackQuery):
    await call.answer("Пока что свободных вакансий нет")
