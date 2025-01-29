"""Пути пользоватлея"""
from aiogram import Router, F
from aiogram.types import Message

from ..keyboards.keyboard import keyboard_servise, keyboard_main

dp = Router()


@dp.message(F.text == 'Список услуг')
async def list_services(message: Message):
    await message.answer("""
                        Список наших услуг:
1 - Услуга 1
2 - Услуга 2
3 - Услуга 3
4 - Услуга 4
""", reply_markup=keyboard_servise)


@dp.message(F.text == 'Услуга 1')
async def services_info_1(message: Message):
    await message.answer('Информация о услуге 1')


@dp.message(F.text == 'Услуга 2')
async def services_info_2(message: Message):
    await message.answer('Информация о услуге 2')


@dp.message(F.text == 'Услуга 3')
async def services_info_3(message: Message):
    await message.answer('Информация о услуге 3')


@dp.message(F.text == 'Услуга 4')
async def services_info_4(message: Message):
    await message.answer('Информация о услуге 4')    


@dp.message(F.text == 'Меню')
async def main(message: Message):
    await message.answer("""
    Привет! Я бот по предоставлении услуг!
Чем могу помочь?
    """, reply_markup=keyboard_main)


@dp.message(F.text == 'Компания')
async def company(message: Message):
    await message.answer('Инфо о компании', reply_markup=keyboard_main)


@dp.message(F.text == 'Контакты')
async def сontacts(message: Message):
    await message.answer('Инфо о контактах', reply_markup=keyboard_main)
