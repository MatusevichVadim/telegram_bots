from aiogram.fsm.state import StatesGroup, State


class Language(StatesGroup):
    choosing_language = State()
