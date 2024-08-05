from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

TOKEN = 7252679351:AAE_nqbKrzZhevl8FkJWtlxw6KDfiGHo2IA

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to JBunny & Boosey Game!')

def send_gif(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    gif_url = 'https://github.com/SolShark1/jbunny-web/raw/main/boosey%20raw.gif'
    context.bot.send_animation(chat_id=chat_id, animation=gif_url)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('send_gif', send_gif))

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()