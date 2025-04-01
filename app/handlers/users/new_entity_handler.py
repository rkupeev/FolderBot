import asyncio
import asyncpg

from datetime import datetime
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from app.fsm.states import NoteState


entity_router = Router()

@entity_router.message(Command("add"))
async def entity_title(message: Message, state: FSMContext):
    await message.answer(
        text='1️⃣Введите заголовок новой записи:',
        reply_markup=None)
    await state.set_state(NoteState.title)


@entity_router.message(NoteState.content_state)
async def entity_content(message: Message, state: FSMContext):
    await message.answer("✅ Заголовок успешно принят!")
    await message.answer("2️⃣Введите текст записи:")
    await state.set_state(NoteState.content_state)

