from aiogram import Dispatcher

from app.presentation.tg_bot.handlers.start import router as start_router, start_dialog


def setup_routers(dp: Dispatcher) -> None:
    dp.include_router(start_router)


def setup_dialogs(dp: Dispatcher) -> None:
    dp.include_router(start_dialog)


def setup_all_handlers(dp: Dispatcher) -> None:
    setup_routers(dp)
    setup_dialogs(dp)


__all__ = ["setup_all_handlers"]
