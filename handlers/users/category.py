from telebot import types

from loader import bot
from db.category import show_products, show_id_products
from keyboards.inline.categories import keyboards_id_product
from settings import add_text


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("category_"))
def callback_answer(callback_query: types.CallbackQuery):
    category = callback_query.data.split("_")[1]
    products = show_products(category)
    string = '\n'.join(f'{product[0]}.{product[1]}\nЦена {product[2]}₽\n' for product in products)
    selected_id = show_id_products(category)
    bot.send_message(callback_query.from_user.id, string + "\n"+ add_text, reply_markup=keyboards_id_product(selected_id))
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)
