from telebot import types


def keyboards_cart_clear():
    markup = types.InlineKeyboardMarkup(row_width=1)
    clear_button = types.InlineKeyboardButton(text="Очистить корзину", callback_data="clear")
    url_button = types.InlineKeyboardButton(text="Перейти в чат с менеджером", url="https://wa.me/79141581222")
    markup.add(url_button, clear_button)
    return markup


def keyboards_cart_add(count_product, product_id):
    buttons = [types.InlineKeyboardButton(text='-', callback_data=f"cart_-_{count_product}_{product_id}"),
               types.InlineKeyboardButton(text=f'{count_product}', callback_data="cart_count_1"),
               types.InlineKeyboardButton(text='+', callback_data=f"cart_+_{count_product}_{product_id}")]
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    keyboard.add(types.InlineKeyboardButton(text="Отправить️", callback_data=f"cart_send_{count_product}_{product_id}"))
    return keyboard


def keyboards_change():
    markup = types.InlineKeyboardMarkup(row_width=2)
    change_button = types.InlineKeyboardButton(text="Изменить цену", callback_data="change")
    add_product = types.InlineKeyboardButton(text="Добавить позицию", callback_data="add_product")
    delete_product = types.InlineKeyboardButton(text="Удалить позицию", callback_data="delete_product")
    info_users = types.InlineKeyboardButton(text="Количество пользователей", callback_data="count_users")
    exit_button = types.InlineKeyboardButton(text="Выход", callback_data="exit")
    markup.add(change_button, add_product, delete_product, info_users, exit_button)
    return markup


def keyboards_change2():
    markup = types.InlineKeyboardMarkup(row_width=1)
    change_button = types.InlineKeyboardButton(text="Изменить цену", callback_data="change2")
    exit_button = types.InlineKeyboardButton(text="Выход", callback_data="exit")
    markup.add(change_button, exit_button)
    return markup
