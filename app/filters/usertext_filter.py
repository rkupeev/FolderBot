
from aiogram.types import Message
from aiogram.filters import BaseFilter
from dataclasses import dataclass

@dataclass
class ABC:
    chars : str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789"


class ContentFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text[0] in ABC.chars
