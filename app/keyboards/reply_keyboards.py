from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton



def show_menu() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text='👤 Профиль'),
        KeyboardButton(text='🗂 Записи')
    )
    builder.add(
        KeyboardButton(text="ℹ️ Помощь")
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def cnacel_menu() -> ReplyKeyboardBuilder: 
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text='❌ Отмена')
    )
    return builder.as_markup(resize_keyboard=True)

