from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import DialogManager, Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Select, Button
from aiogram_dialog.widgets.text import Const, Format
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from app.application.operations.queries.carpet.get_many import GetCarpets
from app.presentation.tg_bot.consts import START_TEXT
from app.presentation.tg_bot.states import StartSG


router = Router()


@inject
async def get_carpet_catalog(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
    action: FromDishka[GetCarpets],
):
    output_data = await action.execute()
    for data in output_data:
        print(data.title)


async def full_name_getter(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    return {"full_name": event_from_user.full_name}


start_dialog = Dialog(
    Window(
        Format(text=START_TEXT),
        Button(
            text=Const("🛒 Каталог"),
            id="catalog",
            on_click=get_carpet_catalog,
        ),
        Button(
            text=Const("📞 Связь с менеджером"),
            id="manager_link",
        ),
        Button(
            text=Const("ℹ️ О магазине"),
            id="about_shop",
        ),
        state=StartSG.start,
        getter=full_name_getter,
    ),
)


@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        mode=StartMode.RESET_STACK,
        state=StartSG.start,
    )
