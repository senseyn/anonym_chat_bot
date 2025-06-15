import logging
# =========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage  # БИБЛИОТЕКА ДЛЯ ХРАНЕНИЯ ДАННЫХ В ОПЕРАТИВНОЙ ПАМЯТИ
# from aiogram.fsm.storage.redis import RedisStorage #ЛУЧШИЙ ВАРИАНТ ДЛЯ ПРОДАКШЕНА
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# ==========ИМПОРТ МОИХ ФАЙЛОВ=========
from settings_conf import load_config

# # # from db_handler.db import PostgresHandler
#=====================================
#redis = Redis.from_url(config("REDIS_URL"))

cfg = load_config()

logging.basicConfig(level=logging.INFO, format="\033[1;30;47m%(asctime)s - %(name)s - %(levelname)s - %("
                                               "message)s\033[0m",
                    datefmt='%Y-%m-%d %H:%M:%S')  # Формат: ГГГГ-ММ-ДД ЧЧ:ММ:СС
logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler(timezone=cfg.scheduler.timezone)
admins = cfg.bot.admins
bot = Bot(token=cfg.bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())  #ОБРАБОТЧИК СООБЩЕНИЙ СОХРАНЯЕТ ДАННЫЕ В ОПЕРАТИВНОЙ ПАМЯТИ
#dp = Dispatcher(storage=storage_redis)  #ОБРАБОТЧИК СООБЩЕНИЙ СОХРАНЯЕТ ДАННЫЕ В REDIS
