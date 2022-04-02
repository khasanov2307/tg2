import sqlite3
import telebot
from telebot import types

from settings import API_KEY, DEBUG, info
import logging

bot = telebot.TeleBot(API_KEY)
conn = sqlite3.connect('price.db', check_same_thread=False)
cursor = conn.cursor()

if DEBUG:
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)

cache = 0

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
    cursor.execute(
        f'select products.name, count(*)*products.price, count(*), price from shopping_cart'
        f' join products on shopping_cart.product_id = products.id where user_id=\'{message.from_user.id}\' group by products.id')
    conn.commit()
    cart = cursor.fetchall()
    cart = '\n'.join(f'{item[0]}\nКоличество:{item[2]}\nЦена за ед.:{item[3]}\nОбщая сумма:{item[1]}₽\n' for item in cart)
    inMurkup = types.InlineKeyboardMarkup(row_width=1)
    inMurkup.add(types.InlineKeyboardButton(text="Очистить корзину", callback_data="clear"))
    bot.send_message(message.chat.id, cart, reply_markup=inMurkup)

def show_categories(message):
    inMurkup = types.InlineKeyboardMarkup(row_width=2)
    cursor.execute("select distinct category from products order by category ASC")
    conn.commit()
    categories = cursor.fetchall()
    print(categories)
    buttons = []
    for category in categories:
        buttons.append(types.InlineKeyboardButton(category[0], callback_data=f'category_{category[0]}'))
    inMurkup.add(*buttons)
    bot.send_message(message.chat.id, "Категории", reply_markup=inMurkup)


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("category_"))
def callback_answer(callback_query: types.CallbackQuery):
    print(callback_query.from_user.id)
    category = callback_query.data.split("_")[1]
    cursor.execute(f"SELECT id, name, price FROM products where category = '{category}'")
    conn.commit()
    result = cursor.fetchall()
    print(result)
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
    buttons = []
    buttons.append(types.InlineKeyboardButton(text='-', callback_data=f"cart_-_1_{product_id}"))
    buttons.append(types.InlineKeyboardButton(text=f'1', callback_data="cart_count_1"))
    buttons.append(types.InlineKeyboardButton(text='+', callback_data=f"cart_+_1_{product_id}"))
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    keyboard.add(types.InlineKeyboardButton(text="Отправить️", callback_data=f"cart_send_1_{product_id}"))
    bot.send_message(callback_query.from_user.id, 'Введите количество',reply_markup=keyboard)
    conn.commit()

@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("cart"))
def check(callback_query: types.CallbackQuery):
    callback = callback_query.data.split('_')
    buttons = []
    count_product = callback[2]
    product_id = callback[3]
    if callback[1] == 'send':
        for i in range(int(count_product)):
            print(count_product)
            cursor.execute("INSERT INTO shopping_cart (user_id, product_id) VALUES(?, ?)",
                                    (callback_query.from_user.id, int(product_id)))
        bot.edit_message_text('Продукт добавлен в корзину', callback_query.from_user.id, callback_query.message.message_id)
        conn.commit()
        return
    if callback[1] == '+':
        count_product = int(count_product) + 1
    elif callback[1] == '-':
        if int(count_product) <= 0:
            bot.send_message(callback_query.from_user.id, '<0')
            return
        count_product = int(count_product) - 1
    buttons.append(types.InlineKeyboardButton(text='-', callback_data=f"cart_-_{count_product}_{product_id}"))
    buttons.append(types.InlineKeyboardButton(text=f'{count_product}', callback_data="cart_count_1"))
    buttons.append(types.InlineKeyboardButton(text='+', callback_data=f"cart_+_{count_product}_{product_id}"))
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    keyboard.add(types.InlineKeyboardButton(text="Отправить️", callback_data=f"cart_send_{count_product}_{product_id}"))
    bot.edit_message_text('Введите количество', callback_query.from_user.id, callback_query.message.message_id, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda c: c.data == "clear")
def clear(callback_query: types.CallbackQuery):
    cursor.execute(f"DELETE FROM shopping_cart WHERE user_id = {callback_query.from_user.id}")
    bot.answer_callback_query(callback_query.id, text="Корзина очищена")
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)
    conn.commit()


if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
       bot.polling(none_stop=True) # запуск бота
    except Exception as e:
       print(e) # или import traceback; traceback.print_exc() для печати полной инфы
