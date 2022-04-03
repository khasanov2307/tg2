from telebot import types

from loader import bot
from db.cart import add_product, clear_cart
from keyboards.inline.cart import keyboards_cart_add


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("bascket"))
def add_to(callback_query: types.CallbackQuery):
    product_id = callback_query.data.split("_")[1]
    bot.send_message(callback_query.from_user.id, 'Введите количество', reply_markup=keyboards_cart_add(1, product_id))


@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("cart"))
def add_to_stage(callback_query: types.CallbackQuery):
    callback = callback_query.data.split('_')
    operand = callback[1]
    count_product = callback[2]
    product_id = callback[3]
    if operand == 'send':
        add_product(count_product, callback_query, product_id)
        bot.edit_message_text('Продукт добавлен в корзину', callback_query.from_user.id,
                              callback_query.message.message_id)
        return
    if operand == '+':
        count_product = int(count_product) + 1
    elif operand == '-':
        if int(count_product) <= 0:
            bot.send_message(callback_query.from_user.id, '<0')
            return
        count_product = int(count_product) - 1

    bot.edit_message_text('Введите количество', callback_query.from_user.id, callback_query.message.message_id,
                          reply_markup=keyboards_cart_add(count_product, product_id))


@bot.callback_query_handler(func=lambda c: c.data == "clear")
def clear(callback_query: types.CallbackQuery):
    clear_cart(callback_query)
    bot.answer_callback_query(callback_query.id, text="Корзина очищена")
    bot.delete_message(chat_id=callback_query.message.chat.id,
                       message_id=callback_query.message.message_id)
