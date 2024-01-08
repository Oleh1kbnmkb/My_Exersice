from aiogram.filters.command import Command
from main3 import bot, dp
from aiogram.types import Message



@dp.message(Command("start"))
async def start(message: Message):
  await message.answer("Hi")