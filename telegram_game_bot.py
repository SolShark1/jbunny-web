from dotenv import load_dotenv
import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater

# Load environment variables
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
WALLET_SEED_PHRASE = os.getenv('WALLET_SEED_PHRASE')

# Debugging statements to ensure the environment variables are loaded
print(f"TOKEN: {TOKEN}")
print(f"WALLET_SEED_PHRASE: {WALLET_SEED_PHRASE}")

# Game state
user_taps = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the game! Tap the button 10 times to win.')

def tap(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_taps[user_id] = user_taps.get(user_id, 0) + 1

    if user_taps[user_id] >= 10:
        update.message.reply_text('Congratulations! You earned 10 JBunny tokens.')
        user_taps[user_id] = 0  # Reset the tap count
        # Logic to award tokens using WALLET_SEED_PHRASE
        reward_user_with_tokens(user_id)
        # Send the image
        with open('boosey raw.gif', 'rb') as photo:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
    else:
        update.message.reply_text(f'Tap count: {user_taps[user_id]}')

def reward_user_with_tokens(user_id):
    # Placeholder for logic to transfer JBunny tokens from the wallet
    # This function should interact with the blockchain or token management system
    print(f"Rewarding user {user_id} with tokens using wallet seed phrase: {WALLET_SEED_PHRASE}")

def main():
    print("Starting bot...")  # Debugging statement
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('tap', tap))

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()
    