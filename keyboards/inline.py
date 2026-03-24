from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.gettext import locales, _

def auto_detected_lang(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=_("select_detected_lang", lang), callback_data="lang_"+lang)],
        [InlineKeyboardButton(text=_("select_other_lang", lang), callback_data="lang_menu")]
    ])

def lang_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for lang in locales:
        builder.button(text=_("name", lang), callback_data="lang_"+lang)

    builder.adjust(1)
    return builder.as_markup()
