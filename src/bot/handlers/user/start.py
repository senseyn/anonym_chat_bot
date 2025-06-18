#=========БИБЛИОТЕКИ СТАНДАРТ========
import asyncio

from aiogram import Router, F  # - магический фильтр
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from aiogram.fsm.context import FSMContext
from src.bot.states.menu_states import MenuStates

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from create_bot import bot
from src.bot.handlers.user.style_text_user import bot_text_baner
from src.bot.db.users_csv import add_user_check, user_registration_date

#======================================
start_router = Router()


#==========ФУНКЦИИ=====================
def delete_mess_commands(error):
    print(f"\033[1;41mОшибка удаления\033[0m: {error}")


#======================СОЗДАНИЕ СПИСКА КОМАНД====================
async def set_commands():
    commands = [BotCommand(command='search', description='🔍 Поиск собеседника'),
                BotCommand(command='stop', description='❌ Закончить диалог с собеседником'),
                BotCommand(command='start', description='🔄 Перезапуск бота'),
                BotCommand(command='interests', description='📝 Выбрать интересы'),
                BotCommand(command='help', description='❔Помощь по боту'),
                BotCommand(command='vip', description='💎 VIP-статус'),
                BotCommand(command='paysupport', description='💰 Помощь по оплате'),
                BotCommand(command='settings', description='⚙️ Настройки профиля'),
                BotCommand(command='rules', description='📙 Правила общения в чате'),
                BotCommand(command='myid', description='🆔 Отобразить ID аккаунта'),
                BotCommand(command='hidden', description='🔓 скрытые команды')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


#======================КОМАНДЫ БОТА==============================
@start_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear() # очистка всех состояний
    await state.set_state(MenuStates.Main) # переход в состояние маин
    add_user_check(message.from_user)  # проверяем или заносим в базу CSV
    date_reg = user_registration_date(str(message.from_user.id))  # получаем дату регистрации
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
        delete_mess_commands(e)
    # ================================
    name = message.from_user.first_name  # Достаем имя пользователя
    text = bot_text_baner(name, date_reg)  # ОТПРАВЛЯЕМ И ПРИНИМАЕМ ТЕКСТ С ПАРАМЕТРОМ NAME И ДАТОЙ РЕГ
    await message.answer(text, parse_mode="HTML")


#==============ОТВЕТ НА ОБЫЧНЫЙ ТЕКСТ====================
@start_router.message(F.text.lower() == "привет", MenuStates.Main)
async def tests(message: Message, state: FSMContext):
    await state.set_state(MenuStates.Main)
    # curr_state = await state.get_state()
    # await message.answer(f"Вы в состоянии: {curr_state}")
    await message.answer("пп а")
