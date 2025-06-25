#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from src.handlers.user.style_text_user import help_text_user
from src.keyboards.user_kb import start_search_button
from src.states.menu_states import MenuStates
#======================================
main_router = Router()


#==========ФУНКЦИИ=====================
async def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================КОМАНДЫ БОТА==============================
@main_router.message(Command('interests'), MenuStates.Main)
async def main_interests(message: Message):
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        await delete_mess_commands(e)
    # ================================
    await message.answer("Интересы", parse_mode="HTML")


@main_router.message(Command('help'), MenuStates.Main)
async def main_help(message: Message):
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        await delete_mess_commands(e)
    # ================================
    name = message.from_user.first_name  # Достаем имя пользователя
    text = await help_text_user(name)
    await message.answer(text, parse_mode="HTML")


@main_router.message(F.text.in_(["💎 Купить VIP", "/vip"]), MenuStates.Main)
async def main_vip(message: Message):
    button = await start_search_button()
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        await delete_mess_commands(e)
    # ================================
    await message.answer("Купить VIP - в разработке", parse_mode="HTML", reply_markup=button)


@main_router.message(Command('paysupport'), MenuStates.Main)
async def main_paysupport(message: Message):
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        await delete_mess_commands(e)
    # ================================
    await message.answer("Помощь по оплате", parse_mode="HTML")


@main_router.message(F.text.in_(["⚙️ Настройки профиля", "/settings"]), MenuStates.Main)
async def main_settings(message: Message):
    button = await start_search_button()
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        await delete_mess_commands(e)
    # ================================
    await message.answer("Настройки", parse_mode="HTML", reply_markup=button)


@main_router.message(Command('rules'), MenuStates.Main)
async def main_rules(message: Message):
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        await delete_mess_commands(e)
    # ================================
    await message.answer("Правила чата", parse_mode="HTML")


@main_router.message(Command('myid'), MenuStates.Main)
async def main_myid(message: Message):
    #========ПЕЧАТАЕТ СТАТУС=========
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.5)
    #========УДАЛЕНИЕ И ПРОВЕРКА======
    try:
        await message.delete()
    except Exception as e:
        await delete_mess_commands(e)
    # ================================
    await message.answer(f"<b>Ваш ID:</b> <pre>{message.chat.id}</pre>", parse_mode="HTML")
