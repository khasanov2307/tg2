from telebot import types


def keyboard_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info = types.KeyboardButton("Информация")
    catalog = types.KeyboardButton("Каталог")
    cart = types.KeyboardButton("Корзина")
    search = types.KeyboardButton("Поиск")
    return markup.add(info, search, cart, catalog)
