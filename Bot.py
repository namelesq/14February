import logging
import asyncio
from aiogram import Bot, Dispatcher, types

# Токен вашего бота
TOKEN = "AAGhct3JX4FYq7V_EWYZJiFmrbR0biTEB68"

# Ссылка на мини-приложение (замените на вашу)
APP_URL = "https://yourusername.github.io/valentine-app/"

# Логирование
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Открыть мини-приложение", web_app=types.WebAppInfo(url=APP_URL))
    )
    await message.answer("Привет! Нажми на кнопку ниже, чтобы открыть мини-приложение:", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())