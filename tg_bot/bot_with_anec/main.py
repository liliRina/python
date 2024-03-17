# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:22:45 2023

@author: Sharlotte
"""
#from parser_for_wall import *
import asyncio
from doyfriend import *
import asyncio
import nest_asyncio


if __name__ == '__main__':    
    print ("Start")
    bot.infinity_polling(skip_pending=True)
    
    bot.stop_bot()
    print ("Stop") 
    