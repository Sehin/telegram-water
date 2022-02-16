import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext, CommandHandler

from arguments import parse_args

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    """Reply on /start command"""
    user = update.effective_user
    update.message.reply_markdown_v2(
        'Hi\!\n'
        'I want to count how much water you drink\.\n'
        'Just send number to me\!\n'
        'If you want to check today value \- use /today command',
        reply_markup=ForceReply(selective=True)
    )

def today(update: Update, context: CallbackContext):
    """Send how much water user drinks today"""
    # in progress
    pass

def main(token: str):
    updater = Updater(token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    args = parse_args()
    main(args.token)