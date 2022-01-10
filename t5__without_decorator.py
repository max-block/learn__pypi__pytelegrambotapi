import os

import telebot
from dotenv import load_dotenv
from telebot.types import Message

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


def cmd1_handler(message: Message):
    bot.reply_to(message, "cmd1 done")


def cmd2_handler(message: Message):
    bot.reply_to(message, "cmd2 done")


bot.add_message_handler({"function": cmd1_handler, "filters": {"commands": ["cmd1"]}})
bot.add_message_handler({"function": cmd2_handler, "filters": {"commands": ["cmd2"]}})

bot.polling()
