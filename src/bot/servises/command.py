from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from create_bot import bot


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


async def hidden_menu_commands(chat_id: int):
    commands = [BotCommand(command='about', description='ℹ️ Информация о боте и авторе'),
                BotCommand(command='roll', description='🔢 Случайное число'),
                BotCommand(command='cat', description='🐈 Получить случайного кота'),
                BotCommand(command='cube', description='🎲 Бросить игральную кость'),
                BotCommand(command='weather', description='🌤 Узнать погоду')]
    await bot.set_my_commands(commands, BotCommandScopeChat(chat_id=chat_id))
