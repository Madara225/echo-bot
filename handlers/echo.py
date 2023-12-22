from aiogram import types, F
from aiogram.filters import CommandStart

from db.users import DataBase
from dispatcher import router, bot

data_base: DataBase = DataBase()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await data_base.add_user(message.chat.id)

    await message.answer(
        (
            "👋 <b>Привет!</b>\n\n"
            "Как только ты отправишь мне сообщение, я сразу же отправлю его всем пользователям.\n\n"
            "Бот создан для общения, обмена контентам и т.д.\n\n"
            "Можете отправлять:\n"
            "— Текстовые сообщения\n"
            "— Медиа (не группы)"
        )
    )


@router.message()
async def echo_handler(message: types.Message):
    users = await data_base.get_users()

    for user in users:
        await bot.copy_message(
            message.chat.id, 
            user, 
            message.message_id
        )