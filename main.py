import asyncio

from aiogram import Dispatcher, Bot, F, types
from aiogram.filters import Command

dp = Dispatcher()
bot = Bot(token="")


@dp.message(Command("start"))
@dp.callback_query(F.data == "start")
async def start(update):
    update_type = type(update)
    if update_type is types.Message:
        await update.answer("Привет! 👋\nЭто бот для продажи курсов по программированию! 🤓\n"
                                "Здесь ты можешь купить интересующие тебя уроки.")
    elif update_type is types.CallbackQuery:
        await update_type.message.edit_text("Привет! 👋\nЭто бот для продажи курсов по программированию! 🤓\n"
                                            "Здесь ты можешь купить интересующие тебя уроки.")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
