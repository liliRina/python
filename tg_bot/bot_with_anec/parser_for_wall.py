# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 23:25:37 2023

@author: Sharlotte
"""
import vk.api
import numpy as np
import vk_api
import configparser
import pandas as pd
from parser_for_poll import *
import time
from bot import *
import sys


def par(owner_id, person_id):
    login = login
    password = password
    session = vk_api.VkApi(login, password)
    session.auth()
    api = session.get_api()
    wall_json=api.wall.get(owner_id=owner_id, offset=0, count=10)['items']
    str_=""
    print ("search")
    for w in wall_json:
        if (len(w['attachments'])!=0):
            for attachment in w['attachments']:
                if (attachment['type']=='poll'):
                    print ("\npost: ", w['text'].strip("\n ").strip(""))
                    str_+="\npost: " + w['text'].strip("\n ").strip("")+"\n"
                    poll_id=attachment["poll"]["id"]
                    print ("poll: ", attachment["poll"]["question"].strip("\n "))
                    str_+="poll: " + attachment["poll"]["question"].strip("\n ")+"\n"
                    if (attachment['poll']['anonymous']==False):
                        if (attachment['poll']['disable_unvote']==False):
                            str_+= parser_for_poll(api, owner_id, poll_id, person_id, 1)
                        else:
                            str_+= parser_for_poll(api, owner_id, poll_id, person_id, 0) 
                    else:
                        str_+="Anonymous"
                        print ("Anonymous")
    print ("str::::", "///////////////////////////n" , "/n", str_)
    return str_
                    
                
                
                
                
                
                
                
                
                
