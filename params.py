# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton
import os

Version = "0.1"
Token = os.environ['TELEGRAM_TOKEN']
AdminList = []
id_list = []
SourceChannelID = []
AdminId = []
StartText = '''StartText'''
HelpMessage = '''HelpMessage'''
WarningMessage = '''WarningMessage'''
DonateText = '''DonateText'''

KeyboardMenu = [[InlineKeyboardButton(text="Donate", callback_data="Donate")],
                [InlineKeyboardButton(text="Help", callback_data="Help")],
                [InlineKeyboardButton(text="Webpage", url="http://www.shaghighi.ir/art/")],
                [InlineKeyboardButton(text="Github", url="https://github.com/sepandhaghighi/art")]]

