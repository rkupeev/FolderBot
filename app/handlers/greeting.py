from aiogram import Router
from aiogram.filters import Command 
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from keyboards.reply_keyboards import show_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в Folder Bot")