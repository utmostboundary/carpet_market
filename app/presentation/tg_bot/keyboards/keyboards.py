from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def row_keyboard_factory(
    buttons: list[KeyboardButton],
    width: int,
) -> ReplyKeyboardBuilder:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(
        *buttons,
        width=width,
    )
    return kb_builder
