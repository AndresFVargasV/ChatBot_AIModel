from telegram import Update
from telegram.ext import CallbackContext, Application, MessageHandler, CommandHandler, filters
import json

with open("config.json", 'r') as f:
    config = json.load(f)

token = config.get('token')

# Define a function that will be called when the /start command is issued.
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am a bot. Please talk to me!')  


def main() -> None:

    # Create the Telegram Application, using the token.
    app = Application.builder().token(token).build()

    # Add a command handler to the Application. This command handler will be Start.
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    # Start the polling
    app.run_polling()

if __name__ == '__main__':
    main()