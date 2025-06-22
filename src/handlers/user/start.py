#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F  # - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.db.users_csv import add_user_check, user_registration_date, user_already_exists
from src.handlers.user.style_text_user import bot_text_baner, bot_text_baner_be
from src.keyboards.user_kb import start_search_button
from src.middlewares.command_setter import set_commands_state
from src.states.menu_states import MenuStates

#======================================
start_router = Router()


#==========ФУНКЦИИ=====================
def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.finish()  # очистка всех состояний
    await state.set_state(MenuStates.Main)  # переход в состояние маин
    keyboard = await start_search_button()
    user_id = str(message.chat.id)
    if user_already_exists(user_id) is False:   # проверяем наличие в базе
        add_user_check(message.from_user)  # проверяем или заносим в базу CSV
        date_reg = user_registration_date(str(message.from_user.id))  # получаем дату регистрации
        await set_commands_state(state, message.chat.id)  # установка команд

        #========ПЕЧАТАЕТ СТАТУС=========
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.TYPING
        )
        await asyncio.sleep(0.5)
        #================================
        name = message.from_user.first_name  # Достаем имя пользователя
        # ОТПРАВЛЯЕМ И ПРИНИМАЕМ ТЕКСТ С ПАРАМЕТРОМ NAME И ДАТОЙ РЕГ
        text = await bot_text_baner(name, date_reg)
        await message.answer(text, parse_mode="HTML", reply_markup=keyboard)

    else:
        date_reg = user_registration_date(str(message.from_user.id))  # получаем дату регистрации
        await set_commands_state(state, message.chat.id)  # установка команд

        # ========ПЕЧАТАЕТ СТАТУС=========
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.TYPING
        )
        await asyncio.sleep(0.5)
        # ================================
        name = message.from_user.first_name  # Достаем имя пользователя
        # ОТПРАВЛЯЕМ И ПРИНИМАЕМ ТЕКСТ С ПАРАМЕТРОМ NAME И ДАТОЙ РЕГ
        text = await bot_text_baner_be(name, date_reg)
        await message.answer(text, parse_mode="HTML", reply_markup=keyboard)


#==============ОТВЕТ НА ОБЫЧНЫЙ ТЕКСТ====================
@start_router.message(F.text.lower() == "привет", MenuStates.Main)
async def tests(message: Message):
    # curr_state = await state.get_state()
    # await message.answer(f"Вы в состоянии: {curr_state}")
    await message.answer("Здарова")
