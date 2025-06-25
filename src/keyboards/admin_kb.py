#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


#=========КЛАВИАТУРЫ=================
async def admin_back():
    button_user_start = [
        [KeyboardButton(text="🔙 В главное меню")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=button_user_start,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_pdlaceholder="ВЫБЕРИ КНОПКУ НИЖЕ"
    )
    return keyboard
