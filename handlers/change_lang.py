from aiogram import Router
from aiogram.types import Message

from database import db
from keyboards.inline import lang_menu
from utils.filters import Text
from utils.gettext import _

router = Router()

@router.message(Text("change_lang"))
async def change_lang(message: Message):
    lang = await db.lang(message.from_user.id)
    await message.answer(_("select_other_lang", lang),
                         reply_markup=lang_menu())
