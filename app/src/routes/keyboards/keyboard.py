from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Список услуг')],
    [KeyboardButton(text='Компания')],
    [KeyboardButton(text='Контакты')],
],
    resize_keyboard=True,
    input_field_placeholder='Управление через меню'
)


keyboard_servise = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Услуга 1')],
    [KeyboardButton(text='Услуга 2')],
    [KeyboardButton(text='Услуга 3')],
    [KeyboardButton(text='Услуга 4')],
    [KeyboardButton(text='Меню')],
],
    resize_keyboard=True,
    input_field_placeholder='Выберите услугу'
)

keyboard_get_info = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Получить обратную связь')],
    [KeyboardButton(text='Меню')],
],
    resize_keyboard=True,
    input_field_placeholder='Выберите команду'
)

keyboard_admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/notice')],
    [KeyboardButton(text='/admin')],
    [KeyboardButton(text='Меню')],
],
    resize_keyboard=True,
    input_field_placeholder='Выберите услугу'
)