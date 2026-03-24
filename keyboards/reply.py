from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.gettext import _

def start_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_("join_test", lang)), KeyboardButton(text=_("question_bank", lang))],
        [KeyboardButton(text=_("vocabulary", lang)), KeyboardButton(text=_("leaderboard", lang))],
        [KeyboardButton(text=_("profile", lang)), KeyboardButton(text=_("change_lang", lang))]
    ], resize_keyboard=True)
