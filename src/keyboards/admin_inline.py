#=========БИБЛИОТЕКИ СТАНДАРТ========
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#=========КЛАВИАТУРЫ=================
keyboard_admin_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔙 В главное меню", callback_data="k_btn_admin_back")]
])
