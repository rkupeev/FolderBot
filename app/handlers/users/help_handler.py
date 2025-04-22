from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.keyboards.menu_keyboard import show_menu

help_router = Router()

@help_router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    await state.clear() 
    await message.answer(
        text=f'Вы используете Folder Bot🤖! \n\nДанный бот позволит хранить текстовые записи небольших размеров в отведенном хранилище. \n\nОсновные команды для бота:\n1. /menu - вызвать меню команд \n2. /profile - открыть профиль \n3. /add - добавить новую запись \n4. /storage - открыть мои записи \n5. /help - получить короткую справку\n\nДля одного пользователя отведено место под хранение 20 записей.\n\n💡 <i>Для корректной работы бота рекомендуем использовать только описанные нами команды. Если во время работы с ботом у вас возникли дополнительные вопросы, задайте их напрямую разработчику (ссылку оставили в био бота)</i>'
    )

