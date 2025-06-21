from aiogram.dispatcher import FSMContext
from aiogram.types import BotCommand, BotCommandScopeChat

# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from create_bot import bot, logger

#======================СОЗДАНИЕ СПИСКА КОМАНД====================0.
COMMANDS_STATE = {
    "Main": [
        BotCommand(command='search', description='🔍 Поиск собеседника'),
        BotCommand(command='stop', description='❌ Закончить диалог с собеседником'),
        BotCommand(command='start', description='🔄 Перезапуск бота'),
        BotCommand(command='interests', description='📝 Выбрать интересы'),
        BotCommand(command='help', description='❔Помощь по боту'),
        BotCommand(command='vip', description='💎 VIP-статус'),
        BotCommand(command='paysupport', description='💰 Помощь по оплате'),
        BotCommand(command='settings', description='⚙️ Настройки профиля'),
        BotCommand(command='rules', description='📙 Правила общения в чате'),
        BotCommand(command='myid', description='🆔 Отобразить ID аккаунта'),
        BotCommand(command='hidden', description='🔓 скрытые команды')
    ],
    "Hidde": [
        BotCommand(command='about', description='ℹ️ Информация о боте и авторе'),
        BotCommand(command='roll', description='🔢 Случайное число'),
        BotCommand(command='cat', description='🐈 Получить случайного кота'),
        BotCommand(command='cube', description='🎲 Бросить игральную кость'),
        BotCommand(command='weather', description='🌤 Узнать погоду'),
        BotCommand(command='start', description='🔄 Главное меню')
    ],
    "Dashboard": [
        BotCommand(command='dashboard', description='Меню админа'),
        BotCommand(command='user_data_id', description='Поиск по ID'),
        BotCommand(command='mailing', description='Рассылка'),
        BotCommand(command='stats_view', description='Статистика')
    ]
}


async def set_commands_state(state: FSMContext, chat_id: int):
    state_stat = await state.get_state()

    # проверка состояния
    if state_stat is None:
        commands = COMMANDS_STATE["Main"]
    else:
        for state_for, commands_list in COMMANDS_STATE.items():
            if state_stat.split(':')[0] == state_for:
                commands = commands_list
                break
        else:
            commands = COMMANDS_STATE["Main"]

    await bot.set_my_commands(commands, scope=BotCommandScopeChat(chat_id=chat_id))
    logger.info(f"Установка команд id {chat_id}, состояние {state_stat}")
