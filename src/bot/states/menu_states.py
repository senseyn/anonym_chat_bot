#====СОЗДАНИЕ ГРУППЫ СОСТОЯНИЙ БОТА====
from aiogram.fsm.state import StatesGroup, State


class MenuStates(StatesGroup):
    Main = State()
    Hidde = State()
