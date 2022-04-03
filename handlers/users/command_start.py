from loader import bot
from db.start import db_start
from keyboards.default.start import keyboard_start


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     "Здравствуйте, {0.first_name}".format(message.from_user),
                     parse_mode='html', reply_markup=keyboard_start())
    db_start(message)
