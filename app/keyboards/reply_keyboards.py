
from aiogram.types import KeyboardButton #, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def show_menu() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="📂Хранилище"),
        KeyboardButton(text="📝Новая запись"),
        KeyboardButton(text="👤Профиль")
    )

    builder.adjust(2)
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Выберите действие")