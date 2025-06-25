#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


#=========КЛАВИАТУРЫ=================
async def start_search_button():
    button_user_search = [
        [KeyboardButton(text="❤️ Начать поиск")],
        {KeyboardButton(text="⚙️ Настройки профиля")},
        [KeyboardButton(text="💎 Купить VIP")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_search,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ ↓"
    )
    return keyboard


async def stop_search_button():
    button_user_search = [
        [KeyboardButton(text="❌ Остановить поиск")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_search,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ ↓"
    )
    return keyboard


async def hidden_back():
    button_user_search = [
        [KeyboardButton(text="🔙 В главное меню")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_search,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ ↓"
    )
    return keyboard


async def null_button_search():
    button_user_search = [
        []
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_search,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard
