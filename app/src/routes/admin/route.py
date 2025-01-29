"""Пути админа."""
from config import config
from aiogram import Router, types, F
from ..keyboards.keyboard import keyboard_admin, keyboard_main
from db import pgsql

dp = Router()


@dp.message(F.text == '/admin')
async def admin_panel(message: types.Message):

    if str(message.from_user.id) == str(config.tgsettings.admin_id):
        await message.reply('Вы в админ панели',
                            reply_markup=keyboard_admin)
    else:
        await message.reply('Извините, я вас не понял',
                            reply_markup=keyboard_main)
