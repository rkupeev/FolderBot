
from aiogram.types import Message
from aiogram.filters import BaseFilter
from dataclasses import dataclass

@dataclass
class ABC:
    data : str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"


class UserTextFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text[0] in ABC.data