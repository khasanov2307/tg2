from db.category import show_category
from db.cart import show_user_cart
from db.search import search_products, search_users
from loader import bot
from keyboards.inline.categories import keyboards_categories, keyboards_id_product
from keyboards.inline.cart import keyboards_cart_clear
from settings import date
import datetime


def show_categories(message):
    categories = show_category()
    keyboard = keyboards_categories(categories)
    bot.send_message(message.chat.id, "Категории. Актуальный прайс на " + date, reply_markup=keyboard)


def show_cart(message):
    cart = show_user_cart(message)
    string_cart = '\n'.join(f'{item[0]}\nКоличество:{item[2]}'
                            f'\nЦена за ед.:{item[3]}₽'
                            f'\nОбщая сумма:{item[1]}₽'
                            f'\n' for item in cart)
    bot.send_message(message.chat.id, string_cart, reply_markup=keyboards_cart_clear())


def send_price(message):
    f = open("file.xlsx", "rb")
    bot.send_document(message.chat.id, f)


def output_search(message):
    name_product = message.text
    products = search_products(name_product1=name_product.lower(), name_product2=name_product.title())
    keyboard = keyboards_id_product(products)
    name_product1 = name_product.lower()
    name_product2 = name_product.title()
    products = search_products(name_product1, name_product2)
    string = '\n'.join(
        f'{product[0]}.{product[1]}\nКатегория:{product[2]}\nЦена {product[3]}₽\n' for product in products)
    bot.send_message(message.from_user.id, string, reply_markup=keyboard)


def send_info(message):
    tmp = message.text
    users = search_users()
    for user in users:
        try:
            bot.send_message(f'{user[0]}', tmp)
        except:
            pass


def logging_history(message):
    dtn = datetime.datetime.now()
    f = open('log.txt', 'a')
    f.write(dtn.strftime("%d-%m-%Y %H:%M") + " " + str(message.from_user.id) + " " + str(message.from_user.first_name)
            + " " + str(message.from_user.last_name) + " " + str(message.text) + "\n")
    f.close()