from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.fsm.states import NoteState

cancel_router = Router()


@cancel_router.message(NoteState.title_state, Command("cancel"))
async def cmd_help(message: Message, state: FSMContext):
    await state.clear() 
    await message.answer(
        text=f'❌ Вы отменили создание новой записи'
    )

@cancel_router.message(NoteState.content_state, Command("cancel"))
async def cmd_help(message: Message, state: FSMContext):
    await state.clear() 
    await message.answer(
        text=f'❌ Вы отменили создание новой записи'
    )


