# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:10:07 2023

@author: Sharlotte
"""

import vk
import numpy as np
import vk_api
import configparser
import pandas as pd
import time


def parser_for_poll (api, owner_id, poll_id, person_id, can_vote):
    poll_json=api.polls.getById(owner_id=owner_id, poll_id=poll_id, extended=0)
    poll_json=poll_json['answers']
    poll=pd.DataFrame(poll_json)
    answers=poll[['id', 'text']]
    answers=answers.to_dict('tight')['data']
    print ("search")
    str_=""
    if (can_vote):
        try:
            api.polls.addVote(owner_id=owner_id, poll_id=poll_id, answer_ids=answers[0][0])
        except:
            api.polls.addVote(owner_id=owner_id, poll_id=poll_id, answer_ids=answers[0][0])
    for [ans, text] in answers:
        bias=0
        try:
            ids=api.polls.getVoters(owner_id=owner_id, poll_id=poll_id, answer_ids=ans, offset=bias)[0]['users']['items']
        except:
            print ("Access to poll denied")
            str_+="Access to poll denied"+"\n"
            break
        while (len(ids)!=0):
            for j in ids:
                if (j==person_id):
                    print ("|||||||||||||||ans: ", text)
                    str_+="|||||||||||||||ans: "+text+"\n"
                    break
            bias+=100
            ids=api.polls.getVoters(owner_id=owner_id, poll_id=poll_id, answer_ids=ans, offset=bias)[0]['users']['items']
    if (can_vote):         
        api.polls.deleteVote(owner_id=owner_id, poll_id=poll_id, answer_ids=answers[0][0])
    return str_