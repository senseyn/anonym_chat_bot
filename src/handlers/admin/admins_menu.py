#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F  # f - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.filters.is_admin import IsAdmin
from src.handlers.admin.style_text_admins import admins_menu_text, admin_back_text
from src.handlers.user.hidden_menu import hidden_router
from src.keyboards.admin_kb import admin_back
from src.keyboards.user_kb import start_search_button
from src.middlewares.command_setter import set_commands_state
from src.states.menu_states import AdminStates, MenuStates

#======================================
admins_router = Router()
admins_router.message.filter(IsAdmin())


#==========ФУНКЦИИ=====================
async def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@admins_router.message(Command('dashboard'))
async def admin_menu_main(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AdminStates.Dashboard)
    await set_commands_state(state, message.chat.id)
    keyboard = await admin_back()
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
        await delete_mess_commands(e)
    # ================================
    text = await admins_menu_text()  # ПРИНИМАЕМ ТЕКСТ
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)


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
        await delete_mess_commands(e)
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
        await delete_mess_commands(e)
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
        await delete_mess_commands(e)
    await message.answer('Статистика бота')


@hidden_router.message(F.text == "🔙 В главное меню", AdminStates.Dashboard)
async def hidden_comand_back_kb(message: Message, state: FSMContext):
    await state.set_state(MenuStates.Main.state)
    await set_commands_state(state, message.chat.id)
    keyboard = await start_search_button()
    text = await admin_back_text()
    # ========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)  # Подтверждаем нажатие кнопки
