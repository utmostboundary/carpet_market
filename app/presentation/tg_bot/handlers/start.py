from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, FSInputFile
from dishka.integrations.aiogram import inject

from app.presentation.tg_bot.keyboards.keyboards import row_keyboard_factory
from app.presentation.tg_bot.lexicon.lexicon import Lexicon

router = Router()


@router.message(CommandStart())
@inject
async def process_start_command(message: Message):
    photo = FSInputFile(path="media/base.png")
    await message.answer_photo(
        photo=photo,
        caption=Lexicon.start.format(username=message.from_user.username),
        reply_markup=row_keyboard_factory(
            [
                KeyboardButton(text=Lexicon.catalog_button),
                KeyboardButton(text=Lexicon.contact_manager_button),
                KeyboardButton(text=Lexicon.about_button),
            ],
            width=2,
        ).as_markup(
            resize_keyboard=True,
            one_time_keyboad=True,
        ),
    )
