# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:56:13 2023

@author: Sharlotte
"""
#pip install bs4
#pip install requests


from bs4 import BeautifulSoup
import requests
from nltk.chat.eliza import eliza_chatbot
from bot import *
from parser_for_wall import *
from telebot import types
import asyncio

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет")
   
@bot.message_handler(commands=['anec'])
def anec(message: types.Message):
    receive = requests.get('http://nekdo.ru/random/')  # отправляем запрос к странице
    page = BeautifulSoup(receive.text, "html.parser")  # подключаем html парсер, получаем текст страницы
    find = page.select('.text')  # из страницы html получаем class="anekdot_text"
    page = (find[0].getText().strip("<"))
    print (page)
    bot.send_message(message.chat.id, page)
    
@bot.message_handler(commands=['citaty'])
def citaty(message: types.Message):   
    receive = requests.get('https://socratify.net/quotes/random')  # отправляем запрос к странице
    page = BeautifulSoup(receive.text, "html.parser")  # подключаем html парсер, получаем текст страницы
    find = page.select('.b-quote__text')  # из страницы html получаем class="anekdot_text"
    page = (find[0].getText().strip("<"))  # из class="anekdot_text" получаем текс и убираем пробелы по сторонам
    print (page)
    bot.send_message(message.chat.id, page)

@bot.message_handler(commands=['stop'])
def stop(message: types.Message):
    bot.send_message(message.chat.id, 'You are not in search!')
    bot.stop_bot()

@bot.message_handler(commands=['parser'])
def parser(message):
    t = message.text.split()[0]
    try:
        owner = message.text.split()[1]
        person = message.text.split()[2]
        bot.send_message(message.chat.id, par(person_id=int(person), owner_id=int(owner)))
    except:
        bot.send_message(message.chat.id, par())
        