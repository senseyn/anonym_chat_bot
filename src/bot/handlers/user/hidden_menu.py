#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router  # - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.bot.states.menu_states import MenuStates

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.bot.handlers.user.style_text_user import hidden_commands_block

#======================================
hidden_router = Router()


#==========ФУНКЦИИ=====================
def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@hidden_router.message(Command('hidden'))
async def hidde_command(message: Message, state: FSMContext):
    await state.set_state(MenuStates.Hidde)
    # ========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    # ========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        delete_mess_commands(e)
    # ================================
    text = hidden_commands_block()  # ПРИНИМАЕМ ТЕКСТ
    await message.answer(text, parse_mode="HTML")


@hidden_router.message(Command('cube'), MenuStates.Hidde)
async def hidde_command(message: Message, state: FSMContext):
    # ========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    # ========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        delete_mess_commands(e)
    await message.answer('🎲')

