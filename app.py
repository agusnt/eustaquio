#!/usr/bin/python3
import telebot
import random
import json
import requests
import os

TOKEN = os.environ['TELEGRAM_KEY']

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
            "gran opción:\n/batman -> para mandarte chistes de BATMAN\n"\
            "/noelia -> pie!!\n/commie -> Proletariados del mundo uníos contra"\
            "el opresor.\n/trump -> Make america great again!!\n/joke -> "\
            "HAHAHAHAHAHAHAHAH.")

@bot.message_handler(commands=['batman'])
def batman(message):
    bot.reply_to(message, batman_json[int(random.random() * len(batman_json))])

@bot.message_handler(commands=['commie'])
def commie(message):
    bot.reply_to(message, comunism_json[int(random.random() * len(comunism_json))])

@bot.message_handler(commands=['noelia'])
def noelia(message):
    if int(random.random() * 2) is 0:
        bot.reply_to(message, "NOELIA QUEREMOS TARTA, AHORA")
    else:
        bot.reply_to(message, "Chorizooooo, 〒▽〒")

@bot.message_handler(regexp="（╯‵□′）╯︵┴─┴")
def table(message):
    bot.reply_to(message, "┬──┬ ﾉ(°—°ﾉ) ")

@bot.message_handler(commands=['trump'])
def trump(message):
    r = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
    bot.reply_to(message, r.json()['message'])

@bot.message_handler(commands=['joke'])
def joke(message):
    r = requests.get("http://tambal.azurewebsites.net/joke/random")
    bot.reply_to(message, r.json()['joke'])
bot.polling()
