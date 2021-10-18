# -*- coding: utf-8 -*-

from art import *

from telegram import InlineKeyboardMarkup, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from random import uniform
import time
import json
import zipfile
import os
import datetime
import logging

from params import *
from functions import make_outputs_dir, art_start


def save_setting(id, access_time):
    config_file_path = os.path.join("outputs", id, "Config.json")
    file = open(config_file_path, "w")
    json.dump({"access_time": str(access_time)}, file)
    file.close()


def load_setting(id):
    try:
        config_file_path = os.path.join("outputs", id, "Config.json")
        file = open(config_file_path, "r")
        data = json.load(file)
        return datetime.datetime.strptime(
            data["access_time"], "%Y-%m-%d %H:%M:%S.%f")
    except Exception:
        return None


def command_handler(bot, update):
    '''
    Check CallBack Query Response From InlineKeyboard Presssing To Run Handlers
    :param bot: Telegram Bot Object
    :param update: Telegram Update Object
    :return: None
    '''
    query = update.callback_query
    user_id = query.from_user.id
    if query.data == "Donate":
        art_donate(bot, query)
    elif query.data == "Help":
        bot.send_message(user_id, HelpMessage)


def check_lang(text):
    for i in text:
        if ord(i) > 127:
            return False
    return True


def text_gen(bot, update):
    '''
    This function generate ascii_art in text file and create ziparchive
    :param bot: Telegram Bot Object
    :type bot: telegram.bot
    :param update: Telegram Update Object
    :type update : telegram.update
    :return: None
    '''
    try:
        access_time_now = datetime.datetime.now()
        font_lists = list(font_map.keys())
        dir_list = os.listdir("outputs")
        chat_id = str(update.message.from_user.id)
        if chat_id not in dir_list:
            os.mkdir(os.path.join("outputs", chat_id))
        access_time_prev = load_setting(chat_id)
        delta_time = 0
        if access_time_prev is None:
            delta_time = 61
        else:
            delta_time = access_time_now - access_time_prev
            delta_time = delta_time.seconds
        if delta_time > 60 or (chat_id in AdminList):
            save_setting(chat_id, access_time_now)
            message_id = update.message.message_id
            bot.send_chat_action(chat_id, action=ChatAction.UPLOAD_DOCUMENT)
            first_name = str(update.message.from_user.first_name)
            last_name = str(update.message.from_user.last_name)
            user_name = str(update.message.from_user.username)

            output_path = os.path.join("outputs", chat_id)
            message_text = update.message.text
            if check_lang(message_text) == False:
                bot.send_message(
                    chat_id=chat_id,
                    text=WarningMessage,
                    reply_to_message_id=message_id)
            zipf = zipfile.ZipFile(
                os.path.join(
                    output_path,
                    first_name +
                    '.zip'),
                'w',
                zipfile.ZIP_DEFLATED)
            for font in font_lists:
                tsave(
                    message_text,
                    filename=os.path.join(
                        output_path,
                        font + ".txt"),
                    print_status=False,
                    font=font)
                zipf.write(
                    os.path.join(
                        output_path,
                        font + ".txt"),
                    font + ".txt")
                os.remove(os.path.join(output_path, font + ".txt"))
            zipf.close()
            output_file = os.path.join(output_path, first_name + ".zip")
            bot.send_document(
                chat_id=chat_id,
                document=open(
                    output_file,
                    'rb'),
                reply_to_message_id=message_id)
            os.remove(output_file)
            if chat_id not in AdminList:
                for admin in AdminList:
                    bot.send_message(
                        int(admin),
                        "ART Alert\nUsername : @" +
                        user_name +
                        "\nFirst Name : " +
                        first_name +
                        "\nLast Name : " +
                        last_name +
                        "\nMessage : " +
                        message_text)
        else:
            update.message.reply_text(
                "Wait " + str(60 - delta_time) + '" For Next Try! ;-)')

    except Exception:
        if os.path.isfile(output_path):
            os.remove(output_path)
        update.message.reply_text("Error In File Creation")


def art_donate(bot, update):
    update.message.reply_text(DonateText)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    make_outputs_dir()
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", art_start))
    updater.dispatcher.add_handler(CommandHandler("donate", art_donate))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, text_gen))
    updater.dispatcher.add_handler(CallbackQueryHandler(command_handler))

    updater.start_polling()
    updater.idle()
