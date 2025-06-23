#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram import Router, F  # - магический фильтр
# from aiogram.enums import ChatAction
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.db.database import Database
from src.keyboards.user_kb import stop_search_button
from src.states.menu_states import MenuStates

#======================================
match_router = Router()

db = Database(r'src/db/db_handler.db') # база данных


@match_router.message(F.text == "❤️ Начать поиск", MenuStates.Main)
async def hidden_comand_back_kb(message: Message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        button = await stop_search_button()
        db.add_queue(chat_id) # ДОБАВЛЕНИЕ В БАЗУ
        await message.answer(f"Поиск собеседника", parse_mode="HTML", reply_markup=button)


