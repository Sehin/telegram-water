import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from arguments import parse_args
from database.database_worker import DatabaseWorker

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

args = parse_args()
db = DatabaseWorker(host=args.dbhost,
                    port=args.dbport,
                    database=args.database,
                    user=args.dbuser,
                    password=args.dbpassword)


def start(update: Update, context: CallbackContext):
    """Reply on /start command"""
    user = update.effective_user
    update.message.reply_markdown_v2(
        'Hi\!\n'
        'I want to count how much water you drank\.\n'
        'Just send number to me\!\n'
        'If you want to check today value \- use /today command'
    )


def set_water_count(update: Update, context: CallbackContext):
    """Append water count to current"""
    user = update.effective_user
    text = update.message.text
    if not text.isdigit():
        update.message.reply_text(
            f'You need to send me water in a milliliters! (it should be digit)'
        )
    else:
        db.add_water(user=user, water_count=int(text))
        update.message.reply_text(
            f'Water has been successfully added! Don\'t give up!'
        )


def today(update: Update, context: CallbackContext):
    """Send how much water user drank today"""
    user = update.effective_user
    today_water = db.get_today_water(user)
    update.message.reply_text(
        f'You drank {today_water} ml'
    )
    pass


def main(args):
    updater = Updater(args.token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("today", today))
    dispatcher.add_handler(MessageHandler(Filters.text, set_water_count))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main(args)
