import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    filename='telegram_bot.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f'lab9 bot')
    logger.info(f"/start command from {user.first_name} {user.last_name} (username: {user.username})")

def echo(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    text = update.message.text
    update.message.reply_text(f'your message {text}')
    logger.info(f"Message from {user.first_name} {user.last_name} (username: {user.username}): {text}")


def main():
    token = '6819550761:AAE0DupQExmQxyYeRUOATSgDV1zCqlKqEMQ'
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
