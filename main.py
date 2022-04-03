from loader import bot
import handlers

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
