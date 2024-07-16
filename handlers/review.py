from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class RestourantReview(StatesGroup):
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


review_router = Router()


@review_router.callback_query(F.data=="feedback")
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await call.message.answer("Как вас зовут?")


@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш инстаграм")
    await state.set_state(RestourantReview.instagram_username)

@review_router.message(RestourantReview.instagram_username)
async def process_instagram(message: types.Message, state: FSMContext):
    await state.update_data(inst_username=message.text)
    await message.answer("Дата вашего посещения нашего заведения")
    await state.set_state(RestourantReview.visit_date)


@review_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.food_rating)
    await state.update_data(visit_date=message.text)
    kb=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Плохо')],
            [types.KeyboardButton(text='Удовлетворительно')],
            [types.KeyboardButton(text='Вкусно')]
        ]
    )
    await message.answer("Как оцениваете качество еды", reply_markup=kb)

@review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):

    if message.text in ('Плохо','Удовлетворительно','Вкусно'):
        await state.update_data(food_rating=message.text)
        await state.set_state(RestourantReview.cleanliness_rating)
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text='Плохо')],
                [types.KeyboardButton(text='Удовлетворительно')],
                [types.KeyboardButton(text='Вкусно')]
            ]
        )
        await message.answer("Как оцениваете чистоту заведения", reply_markup=kb)
    else:
        await message.answer('не понял!!')
        await state.set_state(RestourantReview.food_rating)


@review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):


    kb = types.ReplyKeyboardRemove()

    if message.text in ('Плохо','Удовлетворительно','Вкусно'):
        await state.update_data(cleanliness_rating=message.text)
        await state.set_state(RestourantReview.extra_comments)
        await message.answer("Дополнительные коментарии", reply_markup=kb)
    else:
        await message.answer('не понял!!')
        await state.set_state(RestourantReview.cleanliness_rating)


@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("Спасибо за пройденный отзыв")
    await state.clear()