#!/usr/local/bin/python
import telebot
import random
import json
import os

TOKEN = os.environ['TELEGRAM_KEY']
max_batman = 249

bot = telebot.TeleBot(TOKEN)

#Import batman.json jokes, although they aren't funny
with open('batman.json') as f:
    batman_json = json.load(f)

#Here start the bot
@bot.message_handler(commands=['start', 'help'])
def hello(message):
    bot.reply_to(message, "Hello, yo soy Eustaquio y soy tu bot.\nTengo una "\
            "gran opción:\n /batman -> para mandarte chistes de BATMAN\n"\
            "/noelia -> pie!!")

@bot.message_handler(commands=['batman'])
def batman(message):
    bot.reply_to(message, batman_json[int(random.random() * max_batman)])

@bot.message_handler(commands=['noelia'])
def batman(message):
    bot.reply_to(message, "NOELIA QUEREMOS TARTA, AHORA")

bot.polling()
