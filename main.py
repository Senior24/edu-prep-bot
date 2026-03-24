import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from data.config import BOT_TOKEN
from data.routers import routers_list
from database import db

dp = Dispatcher()

async def main() -> None:
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(BOT_TOKEN, default=default)

    await db.create()

    dp.include_routers(*routers_list)

    print("Bot started")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
