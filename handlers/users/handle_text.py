from db.start import db_start
from loader import bot
from service import show_categories, show_cart, logging_history, send_price
from settings import info, sales
from handlers.users.commands import search


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Каталог':
        show_categories(message)
        logging_history(message)
        db_start(message)
    elif message.text.strip() == 'Информация':
        bot.send_message(message.chat.id, info)
        logging_history(message)
    elif message.text.strip() == 'Корзина':
        show_cart(message)
        logging_history(message)
    elif message.text.strip() == 'Поиск':
        search(message)
        logging_history(message)
    elif message.text.strip() == 'Акции и Скидки':
        bot.send_message(message.chat.id, sales)
        logging_history(message)
    elif message.text.strip() == 'Скачать Прайс':
        send_price(message)
    else:
        bot.send_message(message.chat.id, "Ошибка")