from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.gettext import _

def start_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_("tests", lang)), KeyboardButton(text=_("question_bank", lang))],
        [KeyboardButton(text=_("vocabulary", lang)), KeyboardButton(text=_("leaderboard", lang))],
        [KeyboardButton(text=_("profile", lang)), KeyboardButton(text=_("change_lang", lang))]
    ], resize_keyboard=True)

def tests_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_("host_test", lang)), KeyboardButton(text=_("join_test", lang))],
        [KeyboardButton(text=_("previous_results", lang)), KeyboardButton(text=_("back", lang))]
    ], resize_keyboard=True)

def cancel_button(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=_("cancel", lang), style="danger")]
    ], resize_keyboard=True)
