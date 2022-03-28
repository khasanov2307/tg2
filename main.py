import sqlite3
import telebot
from telebot import types
from Info import info
import logging

bot = telebot.TeleBot("5116135377:AAHzci9w9tHAt3NYle_bjUnVuCJGQTEOq-c")
conn = sqlite3.connect('db_bot', check_same_thread=False)
cursor = conn.cursor()


# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Информация")
    but2 = types.KeyboardButton("Каталог")
    markup.add(but1, but2)
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
    else:
        bot.send_message(message.chat.id, "Ошибка")


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
    cursor.execute(f"SELECT name, price FROM products where category = '{category}'")
    conn.commit()
    result = cursor.fetchall()
    string = '\n'.join(f'{item[0]}\nЦена {item[1]}рублей\n' for item in result)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Назад↩️", callback_data="text1"))
    bot.send_message(callback_query.from_user.id, string, reply_markup=markup)
    bot.delete_message(chat_id=callback_query.message.chat.id,
                          message_id=callback_query.message.message_id)


@bot.callback_query_handler(func=lambda c: c.data == "text1")
def back_to_menu(callback_query: types.CallbackQuery):
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)
    show_categories(callback_query.message)


if __name__ == '__main__':
    bot.infinity_polling()
