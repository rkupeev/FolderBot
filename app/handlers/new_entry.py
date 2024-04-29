from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode

from keyboards.reply_keyboards import show_menu
from filters.usertext_filter import ContentFilter

from db.temp_database import database


router = Router()

class CreateNote(StatesGroup):
    choosing_heading = State()
    choosing_note = State()


@router.message(StateFilter(None), Command("add"))
@router.message(StateFilter(None), F.text == "📝Новая запись")
async def cmd_newentry(message: Message, state: FSMContext):
    await message.answer(
        text="1️⃣ Введите заголовок для новой записи. Заголовок может начинаться только с буквы или цифры! \nДля отмены создания записи введите /cancel.",
        reply_markup=ReplyKeyboardRemove())
    await state.set_state(CreateNote.choosing_heading) 


@router.message(CreateNote.choosing_note, Command("cancel"))
@router.message(CreateNote.choosing_heading, Command("cancel"))
async def any_chosen_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="❌ Вы отменили создание записи",
        reply_markup=show_menu())


@router.message(CreateNote.choosing_heading, Command("profile"))
@router.message(CreateNote.choosing_note, Command("profile"))
async def busy_state(message: Message):
    await message.answer(
        text="⚠️ Вы не можете получить доступ к профилю во время создания записи. Завершите процесс создания или отмените его с помощью команды /cancel."
    )


@router.message(CreateNote.choosing_heading, Command("storage"))
@router.message(CreateNote.choosing_note, Command("storage"))
async def busy_state(message: Message):
    await message.answer(
        text="⚠️ Вы не можете получить доступ к хранилищу во время создания записи. Завершите процесс создания или отмените его с помощью команды /cancel."
    )

@router.message(CreateNote.choosing_heading, 
                ContentFilter())
async def heading_chosen(message: Message, state: FSMContext):
    await state.update_data(chose_heading=message.text)
    await message.answer(
        text='''2️⃣ Теперь введите запись (<i>учтите, что в Telegram присутствует ограничение по количеству символов в одном сообщении</i>). Началом записи должна быть буква или цифра; \nДля отмены создания записи введите /cancel''', parse_mode=ParseMode.HTML)
    await state.set_state(CreateNote.choosing_note)


@router.message(CreateNote.choosing_note)
async def note_chosen(message: Message, state: FSMContext):
    await state.update_data(chose_note=message.text)

    user_data = await state.get_data()
    user_id = message.from_user.id

    database[user_id] = user_data
    print(database)

    await message.answer(
        text=f'✅ Отлично! Вы создали запись с заголовком: <u>{user_data["chose_heading"]}</u>; \nЕё можно будет получить в хранилище',
        reply_markup=show_menu(),
        parse_mode=ParseMode.HTML)
    await state.clear()


@router.message(StateFilter(None), Command("cancel"))
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({}) #data reset
    await message.answer(
        text="⚙️ Данная команда работает только в процессе создания записи...",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(CreateNote.choosing_heading)
async def chosen_incorrectly(message: Message):
    await message.answer(
        text='⚠️ Заголовок не начинается ни с буквы, ни с цифры. Попробуйте снова или отмените создание записи: /cancel')

    