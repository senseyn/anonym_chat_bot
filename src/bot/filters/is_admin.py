#==========ПРОВЕРКА ПРАВ АДМИНА=========
from aiogram.filters import BaseFilter
from aiogram import types
from create_bot import admins


class IsAdmin(BaseFilter):
    async def check(message: types.Message):
        return message.from_user.id in admins