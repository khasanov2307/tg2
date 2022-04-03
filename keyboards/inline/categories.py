from telebot import types


def keyboards_categories(categories):
    buttons = []
    markup = types.InlineKeyboardMarkup(row_width=2)
    for category in categories:
        buttons.append(types.InlineKeyboardButton(category[0], callback_data=f'category_{category[0]}'))
    return markup.add(*buttons)


def keyboards_id_product(selected_id):
    markup = types.InlineKeyboardMarkup(row_width=5)
    buttons = []
    for product_id in selected_id:
        buttons.append(types.InlineKeyboardButton(text=f"{product_id[0]}", callback_data=f"bascket_{product_id[0]}"))
    markup.add(*buttons)
    markup.add(types.InlineKeyboardButton(text="Назад↩️", callback_data="text1"))
    return markup
