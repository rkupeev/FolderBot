import asyncio
import logging, sys
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from app.core import get_settings
from app.handlers import greeting, new_entry

async def main(): 
    bot = Bot(
        get_settings().bot.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=get_settings().bot.PARSE_MODE)
    )
    
    dp = Dispatcher()
    dp.include_routers(
        greeting.router,
        new_entry.router)

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
