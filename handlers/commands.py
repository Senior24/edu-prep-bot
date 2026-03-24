from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from database import db
from keyboards.inline import auto_detected_lang, lang_menu
from utils.gettext import locales, _

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id

    if not await db.check_user(user_id):
        lang = message.from_user.language_code

        if lang in locales:
            await message.answer(_("lang_detected", lang),
                                 reply_markup=auto_detected_lang(lang))
        else:
            await message.answer("💬?", reply_markup=lang_menu())

    else:
        lang = await db.lang(user_id)
        await message.answer(_("start", lang))


@router.callback_query(F.data.startswith("lang"))
async def lang(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data.split("_")[1]

    if data == "menu":
        await callback.message.edit_text(_("select_other_lang", data),
                                         reply_markup=lang_menu())
    else:
        if await db.check_user(user_id):
            pass
        else:
            await db.add_user(user_id, data)
