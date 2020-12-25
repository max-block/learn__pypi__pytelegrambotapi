import os
import time
from threading import Thread

import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


print("start app")
Thread(target=bot.polling).start()

time.sleep(5)
bot.stop_bot()

print("stop app")
