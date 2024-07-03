import asyncio
from aiogram import Bot, Dispatcher, types


bot = Bot(token="6074482966:AAElFQKhA33Fcn1n0B5K0C_MQnpYDzeXVwA")

dp = Dispatcher()

@dp.message()
async def cmd_start(message: types.Message):
    await message.answer(text="Привет")



async def main():
    await dp.start_polling(bot)

asyncio.run(main())