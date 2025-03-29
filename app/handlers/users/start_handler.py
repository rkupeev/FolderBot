
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.keyboards.menu_keyboard import show_menu

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text=f"Добро пожаловать в Folder Bot, {message.from_user.full_name}!\n\nДля быстрого ознакомления введите команду /help или воспользуйтесь встроенным меню команд.",
        reply_markup=show_menu()
        )

