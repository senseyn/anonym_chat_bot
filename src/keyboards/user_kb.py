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


button_user_stop_search = [
    [KeyboardButton(text="❌ Остановить поиск")]
]

button_user_stop = [
    [KeyboardButton(text="➡️ Следующий")],
    [KeyboardButton(text="🚫 Закончить диалог")]
]
