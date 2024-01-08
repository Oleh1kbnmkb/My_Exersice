from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
import asyncio
import os


load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()



async def main():
  from handlers.handlers import start
  dp.message.register(start)
  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()



if __name__ == "__main__":
  asyncio.run(main())
