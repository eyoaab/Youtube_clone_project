import os

import telebot

BOT_TOKEN = os.environ.get("6459012048:AAFwNvIBbinaQ8m-beb6-MY1ySHiB7Oh2kU")

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
