from aiogram import Router
from aiogram.types import Message

from database import db
from keyboards.reply import tests_keyboard
from utils.filters import Text
from utils.gettext import _

router = Router()

@router.message(Text("tests"))
async def tests(message: Message):
    lang = await db.lang(message.from_user.id)
    await message.answer(_("tests_menu", lang), reply_markup=tests_keyboard(lang))
