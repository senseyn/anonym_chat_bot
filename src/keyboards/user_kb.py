#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


#=========КЛАВИАТУРЫ=================
async def start_search_button():
    button_user_start = [
        [KeyboardButton(text="❤️ Начать поиск")],
        {KeyboardButton(text="⚙️ Настройки профиля")},
        [KeyboardButton(text="💎 Купить VIP")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_start,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ ↓"
    )
    return keyboard

async def stop_search_button():
    button_user_start = [
        [KeyboardButton(text="❌ Остановить поиск")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_start,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ ↓"
    )
    return keyboard

async def button_user_search_dialog():
    button_user_dialog = [
        [KeyboardButton(text="➡️ Следующий")],
        [KeyboardButton(text="🚫 Закончить диалог")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_dialog,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ ↓"
    )
    return keyboard

async def hidden_back():
    button_user_start = [
        [KeyboardButton(text="🔙 В главное меню")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_start,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ ↓"
    )
    return keyboard
