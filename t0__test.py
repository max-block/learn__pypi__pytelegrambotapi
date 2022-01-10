import logging
import os

import telebot
from dotenv import load_dotenv

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("z0")
bot = telebot.TeleBot(TOKEN)
print("z1")
bot.send_message(CHAT_ID, "bla bla1")
print("z2")
bot.send_message(CHAT_ID, "bla bla2")
print("z3")
bot.close()
print("z4")
