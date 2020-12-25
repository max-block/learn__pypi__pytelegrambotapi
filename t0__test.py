import os
from pprint import pprint

import telebot
from dotenv import load_dotenv
from telebot.types import Message

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["cmd1"])
def cmd1_handler(message):
    bot.reply_to(message, "cmd1 done")


@bot.message_handler(commands=["cmd2"])
def cmd2_handler(message: Message):
    pprint(message.__dict__)
    bot.reply_to(message, "cmd2 done")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
