import asyncio
import logging

#=========СЕТЕВЫЕ БИБЛИОТЕКИ=========
from aiogram.exceptions import TelegramNetworkError
from aiohttp import ClientConnectorError
#=========БИБЛИОТЕКИ СТАНДАРТ========
from create_bot import bot, dp
#==========ИМПОРТ МОИХ ФАЙЛОВ=========
# роутеры:
from src.handlers.admin.admins_menu import admins_router
from src.handlers.user.hidden_menu import hidden_router
from src.handlers.user.main_menu import main_router
from src.handlers.user.start import start_router
from src.utils.match_engine import match_router

from src.handlers.welcome import print_start_banner
from src.handlers.user.style_text_user import start_text_bot, stop_text_bot



#=====================================
# from work_time.time_func import send_time_msg

# def register_handlers(): #РЕГИСТРАЦИЯ ПРОВЕРКИ НА ПОДПИСКУ
# dp.register_message_handler(cmd_start, commands=['start'])

async def main():
    try:
        #РЕГИСТРИРУЕМ РОУТЕРЫ
        dp.include_router(start_router)
        dp.include_router(hidden_router)
        dp.include_router(admins_router)
        dp.include_router(main_router)
        dp.include_router(match_router)
        #УДАЛЯЕМ ВЕБХУКИ
        await bot.delete_webhook(drop_pending_updates=True)
        # должна быть функция # УСТАНОВКА МЕНЮ КОМАНД
        #ПРИВЕТСТВИЕ БОТА
        await start_text_bot()
        print_start_banner()
        await dp.start_polling(bot)  #СТАРТ БОТА
    except (TelegramNetworkError, ClientConnectorError) as e:
        print("\033[1;41m⚠️ Сетевая ошибка: не удалось подключиться к Telegram API\033[0m")
        logging.error(f"[1;41mОшибка подключения: {e}")
    except Exception as e:
        print("\033[1;41m❌ Произошла непредвиденная ошибка.\033[0m")
        logging.exception(f"Критическая ошибка в работе бота: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        stop_text_bot()
