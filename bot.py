from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
print("бот запущен")

def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, sergei1993valutnii_bot")
    
def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		number = float(text)
		rate = 80.34
		soms = number * rate
		message = "$%.2f = %.2f сом" % (number, soms)
		context.bot.send_message(chat_id=chat.id, text=message)
	except:
 context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода")
 
token ="2124393369:AAEfbl-lPNuvrblZAqi0Fox9dav-kfLSrCY"
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()