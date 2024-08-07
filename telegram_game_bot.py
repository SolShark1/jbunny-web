import os
import logging
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a few command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf'Hi {user.mention_html()}! Welcome to YourTradeBot! Use /connect to connect your wallet.',
        reply_markup=ForceReply(selective=True),
    )

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Simulate wallet connection."""
    try:
        # Simulate wallet authentication
        account = authenticate_with_okto()
        await update.message.reply_text(f'Wallet connected: {account["address"]}')
    except Exception as e:
        await update.message.reply_text(f'Error connecting wallet: {str(e)}')

async def swap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Simulate token swapping."""
    try:
        params = context.args
        if len(params) != 3:
            raise ValueError('Invalid number of parameters. Usage: /swap <fromToken> <toToken> <amount>')
        
        from_token, to_token, amount = params[0], params[1], float(params[2])
        
        # Simulate token swap
        result = swap_tokens(from_token, to_token, amount)
        await update.message.reply_text(f'Swap successful: {result}')
    except Exception as e:
        await update.message.reply_text(f'Error during swap: {str(e)}')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

def authenticate_with_okto():
    """Simulate wallet authentication."""
    return {'address': '0x123456789'}

def swap_tokens(from_token, to_token, amount):
    """Simulate token swap."""
    return {'from': from_token, 'to': to_token, 'amount': amount}

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("connect", connect))
    application.add_handler(CommandHandler("swap", swap))

    # on noncommand i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    application.run_polling()

if name == "__main__":
    main()