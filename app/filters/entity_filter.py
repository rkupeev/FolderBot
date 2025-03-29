from dataclasses import dataclass
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


@dataclass
class Etalon():
    not_allowed = ""
    

class TitleFilter(Filter):
    def __call__(self):
        self.text = self

    async def __call__(self, message: Message, state: FSMContext) -> bool:
        #сверка первой позиции с образцом
        pass

class ContentFilter(Filter):
    pass




#singleton за основу


class CanlelFilter(Filter):
    def __init__(self):
        self.text = 'cancel'

    async def __call__(self, message: Message, state: FSMContext) -> bool:
        return message.text == self.text
    

