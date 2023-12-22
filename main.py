import asyncio

import handlers
from utils.filters import TypeChat
from dispatcher import bot, dp, router
from db.users import DataBase
import os

data_base: DataBase = DataBase()


async def main():
    if not os.path.exists(os.path.join(
        "db", "users.db"
    )):
        await data_base.create_db()

    dp.include_router(router)
    router.message.filter(TypeChat())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
