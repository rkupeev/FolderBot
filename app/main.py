import asyncio
import logging, sys

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from app.handlers import greating 
from app.core.settings import get_settings

dp = Dispatcher()


async def main():
    bot = Bot(token=get_settings().bot.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(
        greating.router
        )

    logging.basicConfig(level=logging.INFO, stream=sys.stdout) #настройка для вывода логов в терминал
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
