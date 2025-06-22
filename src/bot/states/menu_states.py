#====СОЗДАНИЕ ГРУППЫ СОСТОЯНИЙ БОТА====
from aiogram.fsm.state import StatesGroup, State


class MenuStates(StatesGroup):
    Main = State()
    Hidde = State()


class MenuSearch(StatesGroup):
    Search = State()  # меню поиска


class AdminStates(StatesGroup):
    Dashboard = State()  # меню админа
