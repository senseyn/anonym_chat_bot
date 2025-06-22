#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F, types  # - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.bot.handlers.user.start import cmd_start
from src.bot.handlers.user.style_text_user import hidden_commands_block
from src.bot.keyboards.user_inline import keyboard_hidden_menu
from src.bot.middlewares.command_setter import set_commands_state
from src.bot.states.menu_states import MenuStates

#======================================
hidden_router = Router()


#==========ФУНКЦИИ=====================
def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@hidden_router.message(Command('hidden'))
async def hidde_command(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(MenuStates.Hidde)
    await set_commands_state(state, message.chat.id)
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
    text = await hidden_commands_block()  # ПРИНИМАЕМ ТЕКСТ
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard_hidden_menu)


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


@hidden_router.callback_query(F.data == "k_btn_hidden_back", MenuStates.Hidde)
async def hidden_comand_back_kb(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(MenuStates.Main.state)
    # ========ПЕЧАТАЕТ СТАТУС=========
    await callback.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)

    await cmd_start(callback.message, state)  # Вызов функции старта
    await callback.answer()  # Подтверждаем нажатие кнопки
