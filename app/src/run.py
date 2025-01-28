"""Точка входа."""
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

bot = Bot('7697036937:AAHBXnGdoInM2nImukX7EcMkqIdhkdC911I')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("""
    Привет! Я бот по предоставлении услуг!
    Какие услуги вас интересуют?
    """)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
