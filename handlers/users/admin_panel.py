from telebot import types
from db.search import count_users
from loader import bot
from service import set_price, output_id, send_info


@bot.callback_query_handler(func=lambda c: c.data == "change")
def insert_price(callback_query: types.CallbackQuery):
    send = bot.send_message(callback_query.from_user.id,
                            "Введите id:")
    bot.register_next_step_handler(send, output_id)


@bot.callback_query_handler(func=lambda c: c.data == "change2")
def insert_price(callback_query: types.CallbackQuery):
    send = bot.send_message(callback_query.from_user.id,
                            "Новая цена:")
    bot.register_next_step_handler(send, set_price)


@bot.callback_query_handler(func=lambda c: c.data == "count_users")
def send_count(callback_query: types.CallbackQuery):
    count = count_users()
    bot.send_message(callback_query.from_user.id, f"Количество пользователей: {count[0]}")


@bot.callback_query_handler(func=lambda c: c.data == "sales")
def send_sales(callback_query: types.CallbackQuery):
    send = bot.send_message(callback_query.from_user.id,
                            "Ввод")
    bot.register_next_step_handler(send, send_info)


@bot.callback_query_handler(func=lambda c: c.data == "exit")
def clear(callback_query: types.CallbackQuery):
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)
