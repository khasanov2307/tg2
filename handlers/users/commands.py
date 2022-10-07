from keyboards.default.start import keyboard_start
from loader import bot
from db.start import db_start
from service import output_search, log_in


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     "Здравствуйте, {0.first_name}".format(message.from_user),
                     parse_mode='html', reply_markup=keyboard_start())
    db_start(message)


@bot.message_handler(commands=['search'])
def search(message):
    send = bot.send_message(message.from_user.id,
                            "Введите слово  для поиска товара:")
    bot.register_next_step_handler(send, output_search)


@bot.message_handler(commands=['admin'])
def admin_service(message):
    send = bot.send_message(message.from_user.id,
                            "Введите пароль:")
    bot.register_next_step_handler(send, log_in)