#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F, types  # f - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.bot.filters.is_admin import IsAdmin
from src.bot.handlers.admin.style_text_admins import admins_menu_text
from src.bot.handlers.user.start import cmd_start
from src.bot.keyboards.admin_inline import keyboard_admin_menu
from src.bot.middlewares.command_setter import set_commands_state
from src.bot.states.menu_states import AdminStates, MenuStates

#======================================
admins_router = Router()
admins_router.message.filter(IsAdmin())


#==========ФУНКЦИИ=====================
def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@admins_router.message(Command('dashboard'))
async def admin_menu_main(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AdminStates.Dashboard)
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
    text = await admins_menu_text()  # ПРИНИМАЕМ ТЕКСТ
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard_admin_menu)


@admins_router.message(Command('user_data_id'), AdminStates.Dashboard)
async def admin_comand_user_id(message: Message):
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
    await message.answer('Введите айди юзера и я покажу его профиль')


@admins_router.message(Command('mailing'), AdminStates.Dashboard)
async def admin_comand_mailing(message: Message):
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
    await message.answer('Рассылка сообщений, отправь мне сообщение!')


@admins_router.message(Command('stats_view'), AdminStates.Dashboard)
async def admin_comand_stats(message: Message):
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
    await message.answer('Статистика бота')


@admins_router.callback_query(F.data == "k_btn_admin_back", AdminStates.Dashboard)
async def admin_comand_back_kb(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(MenuStates.Main.state)
    # ========ПЕЧАТАЕТ СТАТУС=========
    await callback.bot.send_chat_action(
        chat_id=callback.message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    # Вызов функции старта
    await cmd_start(callback.message, state)
    await callback.answer()  # убираем индикатор загрузки пустым сообщением
