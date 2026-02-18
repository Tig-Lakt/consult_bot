from aiogram import types
from aiogram import Router, F

from functions.context import reset_user_context, user_context
from functions.gemini_conn import ask_gemini
from resources import main_kb


router = Router()


@router.message(F.text == "Новый запрос")
async def btn_new_request(message: types.Message):
    await reset_user_context(message.from_user.id)
    await message.answer("Контекст сброшен. О чем хочешь поговорить?", reply_markup=main_kb)


@router.message(F.text)
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    
    # Если контекста еще нет, создаем его
    if user_id not in user_context:
        await reset_user_context(user_id)
       
    try:
        # Отправляем запрос в Gemini с учетом истории
        response = await ask_gemini(message.text, user_id)
        await message.answer(response, reply_markup=main_kb)
    except Exception as e:
        print(f"Ошибка Gemini: {e}")
        await message.answer("Произошла ошибка при генерации ответа. Попробуйте позже.")