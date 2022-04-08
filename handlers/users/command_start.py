from loader import bot
from db.start import db_start
from keyboards.default.start import keyboard_start
from service import output_search

name_product = str("")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     "Здравствуйте, {0.first_name}".format(message.from_user),
                     parse_mode='html', reply_markup=keyboard_start())
    db_start(message)


@bot.message_handler(commands=['search'])
def search(message):
    send = bot.send_message(message.from_user.id,
                            "Введите слово или словосочетание для поиска товара:")
    bot.register_next_step_handler(send, output_search)
