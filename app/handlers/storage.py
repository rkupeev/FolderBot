from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message #, ReplyKeyboardRemove

from app.handlers.new_entry import CreateNote

'''

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from keyboards.reply_keyboards import show_menu
from filters.usertext_filter import UserTextFilter 

from db.temp_database import database'''


router = Router()

@router.message(StateFilter(None), Command("storage"))
@router.message(StateFilter(None), F.text == "📂Хранилище")
async def storage_call(message: Message):
    await message.answer(
        text="⏳ Скоро здесь что-то будет..."
    )

