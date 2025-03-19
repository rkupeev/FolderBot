

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    #await state.clear  
    await message.answer(
        text=f"Добро пожаловать в Folder Bot, {message.from_user.full_name}!\n\nДля быстрого ознакомления введите команду /help или воспользуйтесь встроенным меню команд."
    )


@router.message(Command('help'))
async def cmd_help(message: Message, state: FSMContext): 
    await message.answer('Этот раздел скоро появится...')


@router.message(Command('menu'))
async def cmd_menu(message: Message, state: FSMContext): 
    await message.answer('Этот раздел скоро появится...')





'''
@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text=f'Вы используете Folder Bot🤖! \n\n#️⃣ <b>Разделы меню</b>: \n1. Хранилище — позволяет получить доступ по заголовку или номеру к записи, хранящейся в базе данных бота; \n2. Новая запись  — позволяет создать новую запись и сохранить ее; \n3. Профиль — можно посмотреть краткую информацию (например, username, ваш ID в телеграме, информацию о количестве записей в базе данных или дату регистрации в боте). \n\n⚙️ <b>Основные команды</b>: \nВсе команды доступны в menu слева, но на всякий случай вот: \n1. /start - начало или продолжение работы \n2. /menu - меню основных команд \n3. /help - получение небольшой справки \n4. /add - добавить новую запись \n\n💡 <i>Для корректной работы бота рекомендуем использовать только описанные нами команды. Если есть вопросы, задайте их разработчику (ссылку оставили в био бота)</i>', 
        parse_mode=ParseMode.HTML, 
        reply_markup=ReplyKeyboardRemove()
        )

'''

'''
@router.message(Command("menu"))
async def cmd_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Вы находитесь в меню основных команд", 
        reply_markup=show_menu()
    )'
'''