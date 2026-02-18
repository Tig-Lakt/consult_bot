from aiogram import types
from aiogram.filters.command import Command
from aiogram import Router

from resources import (
    welcome_text,
    main_kb,
)

from functions.context import reset_user_context


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await reset_user_context(message.from_user.id)
    await message.answer(
        welcome_text,
        reply_markup=main_kb
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Просто отправь мне сообщение, и я сгенерирую ответ.\n\n"
        "Команды:\n"
        "/start - Сбросить контекст и начать заново\n"
        "/help - Справка"
    )


