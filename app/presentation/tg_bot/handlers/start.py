from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.presentation.tg_bot.keyboards.keyboards import start_menu_keyboard
from app.presentation.tg_bot.lexicon.lexicon import LEXICON_RU

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        LEXICON_RU.get(message.text),
        reply_markup=start_menu_keyboard().as_markup(
            resize_keyboard=True,
            one_time_keyboad=True,
        ),
    )
