import os
from telegram.ext import Updater, MessageHandler, filters

def echo(update, context):
    """Echoes the received message back to the user."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    """Main function to run the bot."""
    # Create the Telegram Bot updater and dispatcher
    updater = Updater(token=os.environ.get('6039272282:AAGfmJVxNHSzs-QTB0JHfxix72R2gFUYN20'), use_context=True)
    dispatcher = updater.dispatcher

    # Create an echo handler and register it with the dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
