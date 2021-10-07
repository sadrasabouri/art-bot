# -*- coding: utf-8 -*-
from art import *

from telegram import InlineKeyboardMarkup, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

import logging

from params import *
from functions import make_outputs_dir, art_start, command_handler


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    make_outputs_dir()
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", art_start))
    updater.dispatcher.add_handler(CallbackQueryHandler(command_handler))

    updater.start_polling()
    updater.idle()
