from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
WALLET_SEED_PHRASE = os.getenv('WALLET_SEED_PHRASE')

# Debugging: Print environment variables (remove these lines in production)
print(f"TOKEN: {TOKEN}")
print(f"WALLET_SEED_PHRASE: {WALLET_SEED_PHRASE}")

# Game state
user_taps = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to the game! Tap the button 10 times to win.')

async def tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_taps[user_id] = user_taps.get(user_id, 0) + 1

    if user_taps[user_id] >= 10:
        await update.message.reply_text('Congratulations! You earned 10 JBunny tokens.')
        user_taps[user_id] = 0  # Reset the tap count
        # Logic to award tokens using WALLET_SEED_PHRASE
        reward_user_with_tokens(user_id)
        # Send the image
        with open('boosey raw.gif', 'rb') as photo:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
    else:
        await update.message.reply_text(f'Tap count: {user_taps[user_id]}')

def reward_user_with_tokens(user_id):
    # Placeholder for logic to transfer JBunny tokens from the wallet
    # This function should interact with the blockchain or token management system
    print(f"Rewarding user {user_id} with tokens using wallet seed phrase: {WALLET_SEED_PHRASE}")

def main():
    try:
        application = ApplicationBuilder().token(TOKEN).build()
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('tap', tap))
        application.run_polling()
    except Exception as e:
        logger.error(f"Error: {e}")

if name == '__main__':
    main()