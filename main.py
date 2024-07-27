import asyncio

from aiogram import Dispatcher, Bot, F, types
from aiogram.filters import Command

dp = Dispatcher()
bot = Bot(token="6453026810:AAG871LBfaGMwCS-_Iz0yk6fAjxOckG8MdA")
user_balance = 10_000


@dp.message(Command("start"))
@dp.callback_query(F.data == "start")
async def start(update):
    kb = [
        [types.InlineKeyboardButton(text="Каталог", callback_data="catalog")],
        [
            types.InlineKeyboardButton(text="Профиль", callback_data="user"),
            types.InlineKeyboardButton(text="Тех. Поддержка", callback_data="support")
        ],
        [types.InlineKeyboardButton(text="О нас", callback_data="about_us")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    update_type = type(update)
    if update_type is types.Message:
        await update.answer("Привет! 👋\nЭто бот для продажи курсов по программированию! 🤓\n"
                            "Здесь ты можешь купить интересующие тебя уроки.", reply_markup=keyboard)
    elif update_type is types.CallbackQuery:
        await update.message.edit_text("Привет! 👋\nЭто бот для продажи курсов по программированию! 🤓\n"
                                       "Здесь ты можешь купить интересующие тебя уроки.", reply_markup=keyboard)


@dp.callback_query(F.data == "catalog")
async def catalog(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Курс по Python", callback_data="python"),
         types.InlineKeyboardButton(text="Курс по Aiogram", callback_data="aiogram")],
        [types.InlineKeyboardButton(text="Курс по Telebot", callback_data="telebot"),
         types.InlineKeyboardButton(text="Курс по Django", callback_data="django")],
        [types.InlineKeyboardButton(text="Меню", callback_data="start")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Это каталог доступных курсов!\n"
                                     "Выбери интересующий тебя и прочитай описание!", reply_markup=keyboard)


@dp.callback_query(F.data == "python")
async def python(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Купить", callback_data="buy_python")],
        [types.InlineKeyboardButton(text="Меню", callback_data="start")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Этот курс рассказывает об основных типах данных,\n"
                                     "конструкциях и принципах структурного программирования,"
                                     "\nиспользуя версию языка Python.", reply_markup=keyboard)


@dp.callback_query(F.data == "aiogram")
async def aiogram(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Купить", callback_data="buy_aiogram")],
        [types.InlineKeyboardButton(text="Меню", callback_data="start")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        "aiogram — это современный и полностью асинхронный фреймворк для Telegram Bot API,\n"
        "написанного на Python с использованием asyncio и aiohttp. \n"
        "Это поможет вам сделать ваших ботов быстрее и проще.", reply_markup=keyboard)


@dp.callback_query(F.data == "telebot")
async def aiogram(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Купить", callback_data="buy_telebot")],
        [types.InlineKeyboardButton(text="Меню", callback_data="start")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        "Курс по telebot", reply_markup=keyboard)


@dp.callback_query(F.data == "django")
async def django(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text="Купить", callback_data="buy_django")],
        [types.InlineKeyboardButton(text="Меню", callback_data="start")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        "Курс по django", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
