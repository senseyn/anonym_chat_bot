from aiogram.fsm.context  import FSMContext
from aiogram.types import BotCommand, BotCommandScopeChat

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from create_bot import bot, logger

#======================СОЗДАНИЕ СПИСКА КОМАНД====================0.
COMMANDS_STATE = {
    "Main": [
        BotCommand(command='search', description='❤️ Поиск собеседника'),
        BotCommand(command='start', description='🔄 Перезапуск бота'),
        BotCommand(command='interests', description='📝 Выбрать интересы'),
        BotCommand(command='help', description='❔Помощь по боту'),
        BotCommand(command='vip', description='💎 VIP-статус'),
        BotCommand(command='paysupport', description='💰 Помощь по оплате'),
        BotCommand(command='settings', description='⚙️ Настройки профиля'),
        BotCommand(command='rules', description='📙 Правила общения в чате'),
        BotCommand(command='myid', description='🆔 Отобразить ID аккаунта'),
        BotCommand(command='hidden', description='👁 Скрытые команды')
    ],
    "Hidde": [
        BotCommand(command='hidden', description='👁 Меню скрытых команд'),
        BotCommand(command='about', description='ℹ️ Информация о боте и авторе'),
        BotCommand(command='roll', description='🔢 Случайное число'),
        BotCommand(command='cat', description='🐈 Получить случайного кота'),
        BotCommand(command='cube', description='🎲 Бросить игральную кость'),
        BotCommand(command='weather', description='🌤 Узнать погоду'),
        BotCommand(command='start', description='🔙 Главное меню')
    ],
    "Dashboard": [
        BotCommand(command='dashboard', description='📕 Меню админа'),
        BotCommand(command='user_data_id', description='📋 Поиск по ID'),
        BotCommand(command='mailing', description='📨 Рассылка'),
        BotCommand(command='stats_view', description='📊 Статистика'),
        BotCommand(command='backup_db', description='🗄 Файл базы данных'),
        BotCommand(command='start', description='🔙 Главное меню')
    ],
    "Search": [
        BotCommand(command='search', description='➡️ Следующий'),
        BotCommand(command='stop', description='❌ Остановить поиск')
    ]
}


async def set_commands_state(state: FSMContext, chat_id: int):
    state_name = await state.get_state()
    state_key = state_name.split(':')[1] if state_name else "Main"

    commands = COMMANDS_STATE.get(state_key, COMMANDS_STATE["Main"])

    scope = BotCommandScopeChat(chat_id=chat_id)
    # очистка и установка команд
    await bot.delete_my_commands(scope=scope)
    await bot.set_my_commands(commands, scope=scope)

    logger.info(f"Установка команд id {chat_id}, состояние {state_name}")
