from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, message
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.connection import async_session_maker

from app.database.models import Users
from app.database.connection import connection
from app.keyboards.menu_keyboard import show_menu

start_router = Router()

@connection
async def get_or_create_user(telegram_id: int, session: AsyncSession) -> tuple[Users, bool]:
    result = await session.execute(select(Users).where(Users.telegram_id == telegram_id)) 
    user = result.scalar_one_or_none()
    if user:
        return user, False
    else:
        new_user = Users(telegram_id=telegram_id)
        session.add(new_user)
        await session.commit() 
        return new_user, True


@start_router.message(CommandStart())
async def cmd_start(message: message, state: FSMContext):
    await state.clear()
    user, flag = await get_or_create_user(message.from_user.id)
    
    await message.answer_sticker('CAACAgIAAxkBAAIGNmgHhgNH7PsZMq6nR7OVCGKUVsAaAALYDwACSPJgSxX7xNp4dGuYNgQ')

    if flag:
        await message.answer(
        text=f"Добро пожаловать в Folder Bot, {message.from_user.full_name}!\n\nДля быстрого ознакомления введите команду /help или воспользуйтесь встроенным меню команд.",
        reply_markup=show_menu()
        )
    else:
        await message.answer(
            text=f"Рады снова вас видеть, {message.from_user.full_name}!",
            reply_markup=show_menu()
            )
        