#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router  # f - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.bot.states.menu_states import AdminStates
# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.bot.handlers.admin.style_text_admins import admins_menu_text

#======================================
admins_router = Router()


#==========ФУНКЦИИ=====================
def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@admins_router.message(Command('dashboard'))
async def hidde_command(message: Message, state: FSMContext):
    await state.set_state(AdminStates.Dashboard)
    if message.from_user.id in ADMINS:
        await message.answer("Привет, админ 👨‍💻", reply_markup=admin_main_kb)
    else:
        await message.answer("Привет 👋", reply_markup=user_main_kb)
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
    text = admins_menu_text()  # ПРИНИМАЕМ ТЕКСТ
    await message.answer(text, parse_mode="HTML")
