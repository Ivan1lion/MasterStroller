import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from main_folder.handlers import handlers_router


bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.include_router(handlers_router)




async def main():
    # await bot.delete_webhook(drop_pending_updates=True) #команда для пропуска обновлений пока бот был ОФЛАЙН
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")