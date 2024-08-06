# telegram_game_bot.py

from dotenv import load_dotenv
import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

# Load environment variables
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Game state
user_taps = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the game! Tap the button 10 times to win.')

def tap(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_taps[user_id] = user_taps.get(user_id, 0) + 1

    if user_taps[user_id] >= 10:
        update.message.reply_text('Congratulations! You earned 10 tokens.')
        user_taps[user_id] = 0  # Reset the tap count
        # Logic to award tokens goes here
    else:
        update.message.reply_text(f'Tap count: {user_taps[user_id]}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('tap', tap))

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()