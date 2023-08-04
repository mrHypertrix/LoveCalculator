import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the function to calculate love percentage
def calculate_love_percentage(name1, name2):
    # Your love calculation logic here
    # For simplicity, you can use a random number generator or any other simple formula

# Define the command handler for the '/start' command
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Hi! Welcome to the Love Percentage Bot. Please use /calculate command to check the love percentage.')

# Define the command handler for the '/calculate' command
def calculate(update: Update, _: CallbackContext) -> None:
    # Check if the user provided two names separated by a space
    if len(update.message.text.split()) == 3:
        name1, _, name2 = update.message.text.split()
        love_percentage = calculate_love_percentage(name1, name2)
        update.message.reply_text(f'The love percentage between {name1} and {name2} is {love_percentage}%')
    else:
        update.message.reply_text('Please provide two names separated by a space.')

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("5868706821:AAFG_JUGNaB9RsEDvOet22EQsLotaKDrM-U")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command and message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("calculate", calculate))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
