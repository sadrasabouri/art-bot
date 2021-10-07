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
HelpMessage = """Type your text to see its result."""
WarningMessage = """You may input incorrectly. Try again!"""
DonateText = '''DonateText'''

KeyboardMenu = [[InlineKeyboardButton(text="help", callback_data="help")],
                [InlineKeyboardButton(text="webpage", url="http://www.shaghighi.ir/art/")],
                [InlineKeyboardButton(text="github", url="https://github.com/sepandhaghighi/art")]]
