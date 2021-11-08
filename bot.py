from telegram.ext import Updater, CommandHandler

print("бот запущен")

token="2142334978:AAFpJpjcjIBPlIO7WMJYHbd9gr1woKDJopw"
updater = Updater(token, use_context=True)

updater.start_

updater.start_polling()
updater.idle()