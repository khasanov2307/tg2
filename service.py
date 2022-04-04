from db.category import show_category
from db.cart import show_user_cart
from loader import bot
from keyboards.inline.categories import keyboards_categories
from keyboards.inline.cart import keyboards_cart_clear
from settings import date


def show_categories(message):
    categories = show_category()
    keyboard = keyboards_categories(categories)
    bot.send_message(message.chat.id, "Категории. Актуальный прайс на "+date, reply_markup=keyboard)


def show_cart(message):
    cart = show_user_cart(message)
    string_cart = '\n'.join(f'{item[0]}\nКоличество:{item[2]}'
                            f'\nЦена за ед.:{item[3]}₽'
                            f'\nОбщая сумма:{item[1]}₽'
                            f'\n' for item in cart)
    bot.send_message(message.chat.id, string_cart, reply_markup=keyboards_cart_clear())
