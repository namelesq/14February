import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram import Router

TOKEN = "AAGhct3JX4FYq7V_EWYZJiFmrbR0biTEB68"
APP_URL = "https://namelesq.github.io/14February/"
router = Router()
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp['bot'] = bot
keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть мини-приложение", web_app=WebAppInfo(url = "https://namelesq.github.io/14February/"))]
        ]
    )
@router.message()
async def handle_message(message: types.message):
    await message.answer("Привет! Нажми на кнопку ниже, чтобы открыть мини-приложение:", reply_markup=keyboard)
dp.include_router(router)
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())