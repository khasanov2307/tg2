from telebot import types

from loader import bot
from service import show_categories


@bot.callback_query_handler(func=lambda c: c.data == "text1")
def back_to_menu(callback_query: types.CallbackQuery):
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)
    show_categories(callback_query.message)
