import asyncio
import logging, sys

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from app.core.settings import settings
from app.handlers.users.routers import user_router

dp = Dispatcher()


async def main():
    bot = Bot(token=settings.bot.BOT_TOKEN.get_secret_value(), 
              default=DefaultBotProperties(parse_mode=settings.bot.PARSE_MOD)
              )
    dp = Dispatcher()
    dp.include_router(user_router)

    logging.basicConfig(level=logging.INFO, stream=sys.stdout) #настройка для вывода логов в терминал
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
