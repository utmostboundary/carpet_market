from aiogram import Dispatcher
from app.presentation.tg_bot.handlers.start import router as start_router


def setup_aiogram_routers(dp: Dispatcher):
    dp.include_router(router=start_router)
