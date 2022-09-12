from telebot import types


def keyboards_change():
    markup = types.InlineKeyboardMarkup(row_width=2)
    change_button = types.InlineKeyboardButton(text="Изменить цену", callback_data="change")
    add_product = types.InlineKeyboardButton(text="Добавить позицию", callback_data="add_product")
    delete_product = types.InlineKeyboardButton(text="Удалить позицию", callback_data="delete_product")
    info_users = types.InlineKeyboardButton(text="Количество пользователей", callback_data="count_users")
    sales = types.InlineKeyboardButton(text="Объявление", callback_data="sales")
    exit_button = types.InlineKeyboardButton(text="Выход", callback_data="exit")
    markup.add(change_button, add_product, delete_product, info_users, sales, exit_button)
    return markup


def keyboards_change2():
    markup = types.InlineKeyboardMarkup(row_width=1)
    change_button = types.InlineKeyboardButton(text="Изменить цену", callback_data="change2")
    exit_button = types.InlineKeyboardButton(text="Выход", callback_data="exit")
    markup.add(change_button, exit_button)
    return markup