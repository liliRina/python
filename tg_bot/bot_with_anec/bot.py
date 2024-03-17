# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 22:47:06 2023

@author: Sharlotte
"""

from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_handler_backends import State, StatesGroup
from telebot.asyncio_storage import StateMemoryStorage
from telebot import asyncio_filters
import telebot
from telebot import types


token=token
bot = telebot.TeleBot(token, state_storage=StateMemoryStorage())

import sys
print(sys.version)