import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import load_config
from handlers import greeting, new_entry

dp = Dispatcher()

async def main(): 
    config = load_config()
    bot = Bot(token=config.token)
    dp.include_routers(
        greeting.router,
        new_entry.router)

    logging.basicConfig(
        level=logging.DEBUG, 
        filename="logs.log")

    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
