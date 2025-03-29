from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.keyboards.menu_keyboard import show_menu

menu_router = Router()

@menu_router.message(Command('menu'))
async def cmd_menu(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите одну из предложенных ниже команд:",
        reply_markup=show_menu()
    )

