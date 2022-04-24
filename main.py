from loader import bot
import handlers

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, timeout=123)
    except Exception as e:
        print(e)
