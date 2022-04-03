from telebot import types


def keyboards_cart_clear():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="Очистить корзину", callback_data="clear"))
    return markup


def keyboards_cart_add(count_product, product_id):
    buttons = [types.InlineKeyboardButton(text='-', callback_data=f"cart_-_{count_product}_{product_id}"),
               types.InlineKeyboardButton(text=f'{count_product}', callback_data="cart_count_1"),
               types.InlineKeyboardButton(text='+', callback_data=f"cart_+_{count_product}_{product_id}")]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    keyboard.add(types.InlineKeyboardButton(text="Отправить️", callback_data=f"cart_send_{count_product}_{product_id}"))
    return keyboard
