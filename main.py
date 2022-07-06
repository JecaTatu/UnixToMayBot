import os, telebot, urllib, json
from datetime import datetime

bot = telebot.TeleBot(os.environ["SPACE_BOT_TOKEN"])

@bot.message_handler(commands=["date"])
def date(timestamp):
    texto = timestamp.text.split("/date ")[1]
    texto = int(texto)
    date = datetime.fromtimestamp(texto)
    bot.send_message(timestamp.chat.id, f"Essa data é: {date}")

bot.polling()