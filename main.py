import sqlite3
import telebot
from telebot import types

from Info import info
import logging

bot = telebot.TeleBot("5111751267:AAEid2oqxT2EjT_c2YEC_ja7_-fYQlEpEns")
conn = sqlite3.connect('price.db', check_same_thread=False)
cursor = conn.cursor()
print("Bot started")


# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Информация")
    but2 = types.KeyboardButton("Каталог")
    but3 = types.KeyboardButton("Корзина")
    markup.add(but1, but2, but3)
    bot.send_message(message.from_user.id,
                     "Здравствуйте, {0.first_name}".format(message.from_user),
                     parse_mode='html', reply_markup=markup)
    cursor.execute(f"select user_id from users where user_id = {message.from_user.id}")
    conn.commit()
    id = cursor.fetchone()
    print(id)
    if id is None:
        cursor.execute("INSERT INTO users (user_id) VALUES(?)", (message.from_user.id,))
        conn.commit()


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Каталог':
        show_categories(message)
    elif message.text.strip() == 'Информация':
        bot.send_message(message.chat.id, info)
    elif message.text.strip() == 'Корзина':
        show_cart(message)
    else:
        bot.send_message(message.chat.id, "Ошибка")


def show_cart(message):
    cursor.execute(f"select products.name, products.price.db from shopping_cart join products on "
                   f"shopping_cart.product_id = products.id where user_id = '{message.from_user.id}'")
    conn.commit()
    cart = cursor.fetchall()
    cart = '\n'.join(f'{item[0]}\nЦена {item[1]}₽\n' for item in cart)
    inMurkup = types.InlineKeyboardMarkup(row_width=1)
    inMurkup.add(types.InlineKeyboardButton(text="Очистить корзину", callback_data="clear"))
    bot.send_message(message.chat.id, cart, reply_markup=inMurkup)


def show_categories(message):
    inMurkup = types.InlineKeyboardMarkup(row_width=2)
    cursor.execute("select distinct category from products")
    conn.commit()
    categories = cursor.fetchall()
    buttons = []
    for category in categories:
        buttons.append(types.InlineKeyboardButton(category[0], callback_data=f'category_{category[0]}'))
    inMurkup.add(*buttons)
    bot.send_message(message.chat.id, "Категории", reply_markup=inMurkup)


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("category_"))
def callback_answer(callback_query: types.CallbackQuery):
    print(callback_query.from_user.id)
    category = callback_query.data.split("_")[1]
    cursor.execute(f"SELECT id, name, price.db FROM products where category = '{category}'")
    conn.commit()
    result = cursor.fetchall()
    string = '\n'.join(f'{item[0]}.{item[1]}\nЦена {item[2]}₽\n' for item in result)
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    cursor.execute(f"select id from products where category = '{category}'")
    conn.commit()
    selected_id = cursor.fetchall()
    buttons = []
    for id in selected_id:
        buttons.append(types.InlineKeyboardButton(text=f"{id[0]}", callback_data=f"bascket_{id[0]}"))
    keyboard.add(*buttons)
    keyboard.add(types.InlineKeyboardButton(text="Назад↩️", callback_data="text1"))
    bot.send_message(callback_query.from_user.id, string, reply_markup=keyboard)
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)


@bot.callback_query_handler(func=lambda c: c.data == "text1")
def back_to_menu(callback_query: types.CallbackQuery):
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)
    show_categories(callback_query.message)


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("bascket"))
def add_to(callback_query: types.CallbackQuery):
    product_id = callback_query.data.split("_")[1]
    print(callback_query.from_user.id)
    cursor.execute("INSERT INTO shopping_cart (user_id, product_id) VALUES(?, ?)",
                   (callback_query.from_user.id, product_id))
    conn.commit()


@bot.callback_query_handler(func=lambda c: c.data == "clear")
def clear(callback_query: types.CallbackQuery):
    cursor.execute(f"DELETE FROM shopping_cart WHERE user_id = {callback_query.from_user.id}")
    conn.commit()


if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
       bot.polling(none_stop=True) # запуск бота
    except Exception as e:
       print(e) # или import traceback; traceback.print_exc() для печати полной инфы
