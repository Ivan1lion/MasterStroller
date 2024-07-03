import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


bot = Bot(token="6074482966:AAElFQKhA33Fcn1n0B5K0C_MQnpYDzeXVwA")

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(text="Привет")



async def main():
    # await bot.delete_webhook(drop_pending_updates=True) #команда для пропуска обновлений пока бот был ОФЛАЙН
    await dp.start_polling(bot)

asyncio.run(main())