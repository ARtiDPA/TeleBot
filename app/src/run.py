"""Точка входа."""
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from db import pgsql
from config.config import tgsettings

from routes.user.route import dp as route_one
from routes.admin.route import dp as route_two
from routes.keyboards.keyboard import keyboard_main as kb_main


bot = Bot(tgsettings.token)
dp = Dispatcher()


@dp.message(F.text == '/notice')
async def admin_notice(message: types.Message):
    if str(message.from_user.id) == str(tgsettings.admin_id):
        users = pgsql.get_all_user_ids()
        print(users)
        for user_id in users:
            try:
                await bot.send_message(chat_id=int(user_id), text='уведомление')
                await message.reply('Уведомления отправлены')
            except Exception as e:
                print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")
                await message.reply('Ошибка')
    else:
        await message.reply('Извините, я вас не понял',
                            reply_markup=kb_main)


@dp.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    pgsql.register_user(user_id)
    await message.answer("""
    Привет! Я бот по предоставлении услуг!
Чем могу помочь?
    """, reply_markup=kb_main)


async def main():
    dp.include_router(route_one)
    dp.include_router(route_two)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print(pgsql.create_all_tables())
    asyncio.run(main())
