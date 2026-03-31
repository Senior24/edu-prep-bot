from aiogram import Router
from aiogram.types import Message

from database import db
from utils.filters import Text
from utils.gettext import _

router = Router()

@router.message(Text("profile"))
async def profile(message: Message):
    user_id = message.from_user.id
    lang = await db.lang(user_id)
    is_verified = await db.is_verified(user_id)

    if is_verified:
        verify_status = _("verified_user", lang)
    else:
        verify_status = _("not_verified_user", lang)

    await message.answer(_("profile_info", lang).format(
        name=message.from_user.full_name,
        user_id=user_id,
        rating=await db.get_rating(user_id),
        verified=verify_status
    ))
