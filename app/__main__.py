import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from config import get_settings
from handlers import greeting, new_entry


async def main(): 
    bot = Bot(
        get_settings().bot.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=get_settings().bot.PARSE_MODE)
    )
    dp = Dispatcher()
    dp.include_routers(
        greeting.router,
        new_entry.router)

    logging.basicConfig(
        level=logging.DEBUG, 
        filename="logs.log")

    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
