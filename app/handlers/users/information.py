from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.database.connection import connection
from app.database.models import Users
from app.keyboards.reply_keyboards import show_menu
from app.database.models import Entities, Users


information_router = Router()


#help command
@information_router.message(F.text == "ℹ️ Помощь")
@information_router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    await state.clear() 
    await message.answer(
        text=f'Вы используете Folder Bot🤖! \n\nДанный бот позволит хранить текстовые записи небольших размеров в отведенном хранилище. \n\nОсновные команды для бота:\n1. /menu - вызвать меню команд \n2. /cancel - отменить создание записи \n3. /profile - открыть профиль \n4. /add - добавить новую запись \n5. /storage - открыть мои записи \n6. /help - получить короткую справку\n\nДля одного пользователя отведено место под хранение 20 записей.\n\n💡 <i>Для корректной работы бота рекомендуем использовать только описанные нами команды. Если во время работы с ботом у вас возникли дополнительные вопросы, задайте их напрямую разработчику (ссылку оставили в био бота)</i>',
        reply_markup=ReplyKeyboardRemove()
    )


#profile 
@connection
async def get_user(telegram_id: int, session: AsyncSession):
    statement = await session.execute(
        select(Users.added_at).where(Users.telegram_id == telegram_id)
        )
    result = statement.scalar_one_or_none()
    return result



@information_router.message(Command("profile"))
@information_router.message(F.text == "👤 Профиль")
@connection
async def cmd_profile(message: Message, state: FSMContext, session: AsyncSession):
    await state.clear()
    added_at = await get_user(message.from_user.id)
    added_at = added_at.strftime("%d.%m.%Y %H:%M")

    query = await session.execute(
        select(func.count(Entities.id)).join(Users).where(Users.telegram_id == message.from_user.id)
    )
    records = query.scalars().all()
    records_num = len(records)

    await message.answer(
        text=f"Профиль пользователя {message.from_user.full_name}:\n\n<b>📅 Дата регистрации в боте:</b> {added_at}\n<b>*️⃣ Количество записей</b>: {records_num}"
    )


#menu
@information_router.message(Command('menu'))
async def cmd_menu(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите одну из предложенных ниже команд:",
        reply_markup=show_menu()
    )

