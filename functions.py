# -*- coding: utf-8 -*-
import os
from telegram import InlineKeyboardMarkup

from params import KeyboardMenu, StartText, HelpMessage, WarningMessage

def make_outputs_dir():
    """
    Make 'outputs/' directory in current directory.

    :return: None
    """
    if "outputs" not in os.listdir():
        os.mkdir("outputs")

def art_start(update, context):
    """
    Return start command text.

    :param update: telegram update object
    :type update: telegram.update
    :param context: telegram context object
    :type context: CallbackContext
    :return: None
    """
    reply_markup_menu = InlineKeyboardMarkup(KeyboardMenu)
    update.message.reply_text(StartText, reply_markup=reply_markup_menu)

def command_handler(update, context):
    '''
    Check callback query response and run handlers.

    :param update: telegram update object
    :type update: telegram.update
    :param context: telegram context object
    :type context: CallbackContext
    :return: None
    '''
    query = update.callback_query
    user_id = query.from_user.id
    if query.data == "help":
        context.bot.send_message(user_id, HelpMessage)
    else:
        context.bot.send_message(user_id, WarningMessage)
