"""Пользовательские клавиатуры"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#  создаем кнопки
button_products = KeyboardButton('Продукция🦀')
button_gallery = KeyboardButton('Галерея🌅')
button_address = KeyboardButton('Адрес🗺')
button_contacts = KeyboardButton('Контакты📱')


#  создаем клавиатуру из кнопок вместо обычной
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#  добавляем кнопки на клавиатуру в строку
# kb_client.row(button_products, button_gallery).row(button_address, button_contacts)
kb_client.row(button_products).row(button_address, button_contacts)

kb_city = InlineKeyboardMarkup(row_width=2)
inline_btn_city1 = InlineKeyboardButton('Владивосток🌊', callback_data='send_location_1')
inline_btn_city2 = InlineKeyboardButton('Хабаровск🏙️', callback_data='send_location_2')
kb_city.add(inline_btn_city1, inline_btn_city2)

#  callback кнопки для категорий продукции
kb_category_for_show = InlineKeyboardMarkup(row_width=2)
inline_btn_1 = InlineKeyboardButton('Бакалея', callback_data='show Бакалея')
inline_btn_2 = InlineKeyboardButton('Основы для супов', callback_data='show ОсновыДляСупов')
inline_btn_3 = InlineKeyboardButton('Васаби&Водоросли', callback_data='show ВасабиВодоросли')
inline_btn_4 = InlineKeyboardButton('Бамбук', callback_data='show Бамбук')
inline_btn_5 = InlineKeyboardButton('Икра', callback_data='show Икра')
inline_btn_6 = InlineKeyboardButton('Картофель', callback_data='show Картофель')
inline_btn_7 = InlineKeyboardButton('Корейская кухня', callback_data='show КорейскаяКухня')
inline_btn_8 = InlineKeyboardButton('Краб&Гребешок', callback_data='show КГМК')
inline_btn_9 = InlineKeyboardButton('Креветка блочная', callback_data='show КБлок')
inline_btn_10 = InlineKeyboardButton('Креветка мелкая', callback_data='show КМелк')
inline_btn_11 = InlineKeyboardButton('Креветка россыпь', callback_data='show КРоссыпь')
inline_btn_12 = InlineKeyboardButton('Масла', callback_data='show Масло')
inline_btn_13 = InlineKeyboardButton('Молочная продукция', callback_data='show Молочка')
inline_btn_14 = InlineKeyboardButton('Мучная продукция', callback_data='show Мучная')
inline_btn_15 = InlineKeyboardButton('Мясо&Полуфабрикаты', callback_data='show ПФБК')
inline_btn_16 = InlineKeyboardButton('Растения&Грибы', callback_data='show РиГ')
inline_btn_17 = InlineKeyboardButton('Рис', callback_data='show Рис')
inline_btn_18 = InlineKeyboardButton('Рыба ПСГ, ПБГ, С/М', callback_data='РыбаПСГ')
inline_btn_19 = InlineKeyboardButton('Рыба ФИЛЕ СВЕЖЕМОРОЖЕННОЕ', callback_data='РыбаФиле')
inline_btn_20 = InlineKeyboardButton('Главное меню⬇', callback_data='клавиатура')
inline_btn_21 = InlineKeyboardButton('Соевый&Уксус', callback_data='show Соевый')
inline_btn_22 = InlineKeyboardButton('Соусы&Кетчупы', callback_data='show Соусы')
inline_btn_23 = InlineKeyboardButton('Соусы паназиатские', callback_data='show СоусыАзия')
inline_btn_24 = InlineKeyboardButton('Сыр&Майонез', callback_data='show СырМайонез')
inline_btn_25 = InlineKeyboardButton('Ягоды&Овощи&Заморозка', callback_data='ЯгодыОвощи')
kb_category_for_show.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6,
                         inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_10, inline_btn_11, inline_btn_12,
                         inline_btn_13, inline_btn_14, inline_btn_15, inline_btn_16, inline_btn_17, inline_btn_18,
                         inline_btn_19, inline_btn_21, inline_btn_22, inline_btn_23, inline_btn_24,
                         inline_btn_25, inline_btn_20)