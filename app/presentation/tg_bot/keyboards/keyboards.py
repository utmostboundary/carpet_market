from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_menu_keyboard() -> ReplyKeyboardBuilder:
    kb_builder = ReplyKeyboardBuilder()
    catalog_button = KeyboardButton(text="📜 Каталог")
    contact_manager_button = KeyboardButton(text="📞 Связь с менеджером")
    about_shop_button = KeyboardButton(text="ℹ️ О магазине")
    kb_builder.row(
        catalog_button,
        contact_manager_button,
        about_shop_button,
        width=2,
    )
    return kb_builder
