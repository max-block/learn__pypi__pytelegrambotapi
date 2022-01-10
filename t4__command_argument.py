import os

import telebot
from dotenv import load_dotenv
from telebot.types import Message

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["cmd1"])
def cmd1_handler(message: Message):
    bot.send_message(message.chat.id, "cmd1 done")


@bot.message_handler(commands=["cmd2"])
def cmd2_handler(message: Message):
    arg = message.text.removeprefix("/cmd2")
    bot.send_message(message.chat.id, "argument: " + arg)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "unknown command")


bot.polling()
