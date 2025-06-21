#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router  # - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.bot.middlewares.command_setter import set_commands_state
from src.bot.states.menu_states import MenuStates
from src.bot.handlers.user.style_text_user import hidden_commands_block

#======================================
hidden_router = Router()


#==========ФУНКЦИИ=====================
def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@hidden_router.message(Command('hidden'))
async def hidde_command(message: Message, state: FSMContext):
    await state.clear()
    await set_commands_state(state, message.chat.id)
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


@hidden_router.message(Command('about'), MenuStates.Hidde)
async def hidde_command_about(message: Message):
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

    await message.answer('описание бота')
    
    
@hidden_router.message(Command('roll'), MenuStates.Hidde)
async def hidde_command_roll(message: Message):
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
    await message.answer('случайное число')
    
    
@hidden_router.message(Command('cat'), MenuStates.Hidde)
async def hidde_command_cat(message: Message):
    # ========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO
    )
    await asyncio.sleep(0.5)
    # ========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        delete_mess_commands(e)
    await message.answer_photo("https://cataas.com/cat", caption="Котик (˶‾᷄ ⁻̫ ‾᷅˵)")
    
    
@hidden_router.message(Command('cube'), MenuStates.Hidde)
async def hidde_command_cube(message: Message):
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
    await message.answer_dice(emoji='🎲')
    

@hidden_router.message(Command('weather'), MenuStates.Hidde)
async def hidde_command_weather(message: Message):
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
    await message.answer('погода')
    