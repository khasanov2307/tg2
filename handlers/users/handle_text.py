from db.start import db_start
from loader import bot
from service import show_categories, show_cart
from settings import info, sales
from handlers.users.command_start import search


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Каталог':
        show_categories(message)
        db_start(message)
    elif message.text.strip() == 'Информация':
        bot.send_message(message.chat.id, info)
    elif message.text.strip() == 'Корзина':
        show_cart(message)
    elif message.text.strip() == 'Поиск':
        search(message)
    elif message.text.strip() == 'Акции и Скидки':
        bot.send_message(message.chat.id, sales)
    else:
        bot.send_message(message.chat.id, "Ошибка")
