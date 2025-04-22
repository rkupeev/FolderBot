import asyncio

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.connection import connection
from app.database.models import Users

profile_router = Router()


@connection
async def get_user(telegram_id: int, session: AsyncSession):
    statement = await session.execute(
        select(Users.added_at).where(Users.telegram_id == telegram_id)
        )
    result = statement.scalar_one_or_none()
    return result


@profile_router.message(F.text == "👤 Профиль")
@profile_router.message(Command("profile"))
async def cmd_profile(message: Message, state: FSMContext):
    await state.clear()
    added_at = await get_user(message.from_user.id)
    added_at = added_at.strftime("%d.%m.%Y %H:%M")
    records_num = 'Этот раздел профиля скоро будет добавлен...'

    await message.answer(
        text=f"Профиль пользователя {message.from_user.full_name}:\n\n<b>📅 Дата регистрации в боте:</b> {added_at}\n<b>*️⃣ Количество записей</b>: {records_num}"
    )
