#!/usr/bin/python3
import telebot
import random
import json
import os

TOKEN = os.environ['TELEGRAM_KEY']
max_batman = 249
max_commie = 105

bot = telebot.TeleBot(TOKEN)

#Import batman.json jokes, although they aren't funny
with open('json/batman.json') as f1:
    batman_json = json.load(f1)
with open('json/communism.json') as f2:
    comunism_json = json.load(f2)

#Here start the bot
@bot.message_handler(commands=['start', 'help'])
def hello(message):
    bot.reply_to(message, "Hello, yo soy Eustaquio y soy tu bot.\nTengo una "\
            "gran opción:\n /batman -> para mandarte chistes de BATMAN\n"\
            "/noelia -> pie!!\n/commie -> Proletariados del mundo uníos contra"\
            "el opresor.")

@bot.message_handler(commands=['batman'])
def batman(message):
    bot.reply_to(message, batman_json[int(random.random() * max_batman)])

@bot.message_handler(commands=['commie'])
def batman(message):
    bot.reply_to(message, comunism_json[int(random.random() * max_commie)])

@bot.message_handler(commands=['noelia'])
def batman(message):
    bot.reply_to(message, "NOELIA QUEREMOS TARTA, AHORA")

bot.polling()
