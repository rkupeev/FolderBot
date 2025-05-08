from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.keyboards.reply_keyboards import cnacel_menu
from app.keyboards.reply_keyboards import show_menu
from app.fsm.states import NoteState

from app.database.models import Users, Entities
from app.database.connection import connection


entity_router = Router()

#adding a new entity
@connection 
async def create_entity(telegram_id: int, title: str, content: str, session: AsyncSession) -> None:
    result = await session.execute(select(Users.id).where(Users.telegram_id == telegram_id))
    user_id = result.scalar_one()

    template = Entities(user_id=user_id, title=title, content=content)
    session.add(template)

    await session.commit()


@entity_router.message(Command("add"))
@connection
async def entity_title(message: Message, state: FSMContext, session: AsyncSession):
    result = await session.execute(
        select(Entities.id).where(Users.telegram_id == message.from_user.id)
    ) 
    records = result.scalars().all()

    if len(records) >= 20:
        await message.reply('❌ Невозможно добавить запись! Превышен лимит.')
    else:
        await message.answer(
            text='1️⃣ Введите заголовок новой записи:', 
            reply_markup=cnacel_menu())
        await state.set_state(NoteState.title_state)
        

@entity_router.message(NoteState.title_state)
async def entity_content(messge: Message, state: FSMContext):
    await state.update_data(title=messge.text)
    await messge.answer(
        text="✅ Заголовок успешно принят!\n\n2️⃣Введите текст записи:",
        reply_markup=cnacel_menu())
    await state.set_state(NoteState.content_state)


@entity_router.message(NoteState.content_state)
async def ending_of_adding(message: Message, state: FSMContext):
    data = await state.get_data()
    title = data.get("title")
    content = message.text
    telegram_id = message.from_user.id

    await create_entity(telegram_id=telegram_id, title=title, content=content)
    await message.answer(text="🥳 Запись успешно добавлена!",
                         reply_markup=show_menu())
    await state.clear()
 

@entity_router.message(F.text == '❌ Отмена')
@entity_router.message(NoteState.content_state, Command("cancel"))
@entity_router.message(NoteState.title_state, Command("cancel"))
async def cmd_help(message: Message, state: FSMContext):
    await state.clear() 
    await message.answer(
        text=f'❌ Вы отменили создание новой записи',
        reply_markup=ReplyKeyboardRemove()
    )