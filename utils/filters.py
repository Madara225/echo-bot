from aiogram.filters import BaseFilter
from typing import Literal
from aiogram import types


class TypeChat(BaseFilter):
    async def __call__(self, message: types.Message) -> (Literal[True] | None):
        if message.chat.type == "private":
            return True