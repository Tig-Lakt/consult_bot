from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


# Клавиатура с кнопкой сброса
main_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Новый запрос")]],
    resize_keyboard=True
)