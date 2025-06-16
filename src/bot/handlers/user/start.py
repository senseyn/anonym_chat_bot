#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F  # - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand, BotCommandScopeDefault

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from create_bot import bot
from src.bot.handlers.user.style_text_user import bot_text_baner
from src.bot.db.users_csv import add_user_check, user_registration_date

#=====================================
start_router = Router()


#======================СОЗДАНИЕ СПИСКА КОМАНД====================
async def set_commands():
    commands = [BotCommand(command='start', description='перезапуск бота'),
                BotCommand(command='cat', description='картинка кота'),
                BotCommand(command='s', description='тест')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


#======================КОМАНДЫ БОТА==============================
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    add_user_check(message.from_user)  # заносим в базу CSV
    date_reg = user_registration_date(str(message.from_user.id))  # получаем дату регистрации
    await message.delete()
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await asyncio.sleep(0.4)
    name = message.from_user.first_name  # Достаем имя пользователя
    text = bot_text_baner(name, date_reg)  # ОТПРАВЛЯЕМ И ПРИНИМАЕМ ТЕКСТ С ПАРАМЕТРОМ NAME
    await message.answer(text, parse_mode="HTML")


@start_router.message(F.text.lower() == "привет")
async def tests(message: Message):
    await message.answer("ДА ДА ДА")
