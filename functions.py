# -*- coding: utf-8 -*-

import os
import datetime
import json
import random
from telegram import InlineKeyboardMarkup

import art

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

def text_gen(update, context):
    """
    Generate ASCII art.

    :param update: telegram update object
    :type update: telegram.update
    :param context: telegram context object
    :type context: CallbackContext
    :return: None
    """
    chat_id = str(update.message.from_user.id)
    font = random.choice(art.NON_ASCII_FONTS)
    art_out = art.text2art(update.message.text, font=font)
    context.bot.send_message(chat_id, art_out)
