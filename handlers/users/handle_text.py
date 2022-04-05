from loader import bot
from service import show_categories, show_cart
from settings import info
from handlers.users.command_start import search


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Каталог':
        show_categories(message)
    elif message.text.strip() == 'Информация':
        bot.send_message(message.chat.id, info)
    elif message.text.strip() == 'Корзина':
        show_cart(message)
    elif message.text.strip() == 'Поиск':
        search(message)
    else:
        bot.send_message(message.chat.id, "Ошибка")
