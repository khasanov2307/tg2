"""Клиентские диспетчеры"""
from random import randint

from aiogram import types, Dispatcher

from data.sqlite_db import create_profile
from keyboards import client_keyboards
from aiogram.dispatcher.filters import Text
from data import sqlite_db
from loader import bot
from data.config import address, phones, email, names


async def commands_start(message: types.Message):
    """Приветственный хендлер для команд start и help"""
    #  отдаем клавиатуру при команде /start или /help
    await message.answer('Привет! Это бот Амур Хорека!', reply_markup=client_keyboards.kb_client)
    user_id = message.from_user.id
    #print(user_id)
    await create_profile(user_id=user_id)


async def load_address(callback_query: types.CallbackQuery):
    """Хендлер для отображения адреса"""
    await bot.send_message(callback_query.from_user.id, "Наше расположение:", reply_markup=client_keyboards.kb_city)
    # await message.reply('Наше расположение:', reply_markup=client_keyboards.kb_city)
    # await message.reply_location(48.472124, 135.093027)
    # await message.reply(address[0])
    # await message.answer_location(float(address[1]), float(address[2]))


async def load_contacts(message: types.Message):
    await message.reply(address)
#    """Хендлер для отображения контактов"""
#    for name, phone in zip(names, phones):
#        await message.answer_contact(phone_number=phone, first_name=name)
#    await message.answer(email)


async def show_products(message: types.Message):
    """Хендлер для команды 'продукция' отображает категории продукции"""
    await message.reply('Актуальный прайс на 07.09.2023\nВыберите пожалуйста категорию⬇️', reply_markup=client_keyboards.kb_category_for_show)
    await message.delete()


async def show_all_products_from_category(callback_query: types.CallbackQuery):
    """Отображает все товары выбранной категории"""
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Каталог🔙", callback_data="Продукция"))
    category = callback_query.data.replace('show ', '')
    read = await sqlite_db.sql_loads_all_products_from_category(category)
    string = '\n\n'.join(f'{ret[0]}\nЦена {ret[1]}₽' for ret in read)
    await bot.send_message(callback_query.from_user.id, string + "\n\n", reply_markup=keyboard)


async def show_all_photos_from_gallery(message: types.Message):
    """Хендлер для кнопки 'Галерея', отображает все фото из галереи"""
    read = await sqlite_db.sql_loads_all_gallery()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n')


def register_handlers_client(dp: Dispatcher):
    """
        Функция регистратор клиентских диспетчеров, вызывается из main.py
    """
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(load_address, Text(startswith='Адрес'))
    dp.register_message_handler(load_contacts, Text(startswith='Контакты'))
    dp.register_message_handler(show_products, Text(startswith='Продукция'))
    dp.register_callback_query_handler(show_all_products_from_category, lambda x: x.data.startswith('show'))
    dp.register_message_handler(show_all_photos_from_gallery, Text(startswith='Галерея'))

    @dp.callback_query_handler(text="Продукция")
    async def inline_button1(query: types.CallbackQuery):
        await query.message.edit_text('Выберите пожалуйста категорию⬇️',
                                      reply_markup=client_keyboards.kb_category_for_show)
        # await query.message.delete()
        await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id - 1)

    @dp.callback_query_handler(text="send_location_1")
    async def inline_button1(query: types.CallbackQuery):
        await query.message.edit_text('Владивосток🌊')
        await query.message.reply_location(43.147833, 131.920276)


    @dp.callback_query_handler(text="send_location_2")
    async def inline_button1(query: types.CallbackQuery):
        await query.message.edit_text('Хабаровск🏙')
        await query.message.reply_location(48.464131, 135.113805)
