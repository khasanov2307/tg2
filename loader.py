import telebot
import logging
from settings import API_KEY, DEBUG

if DEBUG:
    logger = telebot.logger

    telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_KEY, exception_handler=telebot.ExceptionHandler())


