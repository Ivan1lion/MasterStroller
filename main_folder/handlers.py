from aiogram import types, Router
from aiogram.filters import CommandStart

handlers_router = Router()


@handlers_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(text="Привет")