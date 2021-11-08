from telegram.ext import Updater, CommandHandler

print("бот запущен")

def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, chernov1993 bot")
    
token ="2142334978:AAFpJpjcjIBPlIO7WMJYHbd9gr1woKDJopw"
updater = Updater(token, use_context=True)
dispatcher.add_handler(CommandHandler("start", on_start))


updater.start_polling()
updater.idle()