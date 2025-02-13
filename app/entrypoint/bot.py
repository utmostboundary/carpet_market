import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from dishka.integrations.aiogram import setup_dishka

from app.entrypoint.common import provide_context
from app.entrypoint.ioc import setup_aiogram_di
from app.presentation.tg_bot.setup import setup_aiogram_routers


def get_bot_token() -> str:
    return os.environ.get("BOT_TOKEN")


async def create_bot() -> None:
    context = provide_context()
    session = AiohttpSession()

    bot_settings = {
        "session": session,
        "default": DefaultBotProperties(parse_mode=ParseMode.HTML),
    }
    bot_token = get_bot_token()
    bot = Bot(token=bot_token, **bot_settings)
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher()
    container = setup_aiogram_di(
        context=context,
    )
    setup_dishka(
        container=container,
        router=dp,
        auto_inject=True,
    )
    setup_aiogram_routers(dp=dp)
    await dp.start_polling(bot)


asyncio.run(create_bot())
