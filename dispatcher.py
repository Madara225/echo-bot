from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

router = Router()

bot = Bot("", parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())