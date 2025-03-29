
from aiogram.fsm.state import State, StatesGroup 

class NoteState(StatesGroup):
    title_state = State()
    content_state = State()


