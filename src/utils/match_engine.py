#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F  # - магический фильтр
from aiogram.enums import ChatAction
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.keyboards.user_kb import stop_search_button
from src.states.menu_states import MenuStates

#======================================
match_router = Router()


@match_router.message(F.text == "🔍 Поиск собеседника", MenuStates.Main)
async def hidden_comand_back_kb(message: Message):
    if message.chat.id == "private":
        button = stop_search_button()
    # ========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    await message.answer("1", parse_mode="HTML")  # Подтверждаем нажатие кнопки
