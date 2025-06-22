#==========ПРОВЕРКА ПРАВ АДМИНА=========
from aiogram.filters import BaseFilter
from aiogram.types import Message
from create_bot import admins


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in admins
