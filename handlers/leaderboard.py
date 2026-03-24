from aiogram import Router
from aiogram.types import Message

from database import db
from utils.filters import Text
from utils.gettext import _

router = Router()

@router.message(Text("leaderboard"))
async def display_leaderboard(message: Message):
    data = await db.leaderboard()
    lang = await db.lang(message.from_user.id)

    leaderboard = [f"{number}. {name} | {rating}"
                   for number, (name, rating) in enumerate(data, start=1)]

    leaderboard.insert(0, _("leaderboard", lang) + "\n")

    await message.answer("\n".join(leaderboard))
