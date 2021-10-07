# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton
import os

Version = "0.1"
Token = os.environ['TELEGRAM_TOKEN']
AdminList = []
id_list = []
SourceChannelID = []
AdminId = []
StartText = """Welcome to art bot. Type your text to see its result."""
HelpMessage = '''HelpMessage'''
WarningMessage = '''WarningMessage'''
DonateText = '''DonateText'''

KeyboardMenu = [[InlineKeyboardButton(text="Help", callback_data="Help")],
                [InlineKeyboardButton(text="Webpage", url="http://www.shaghighi.ir/art/")],
                [InlineKeyboardButton(text="Github", url="https://github.com/sepandhaghighi/art")]]
