'''
Created on 2017-10-12

@author: marvin_ma
'''
import json

def act_bet(amount):
    return json.dumps({
                "eventName": "__action",
                "data": {
                         "action": "bet",
                         "amount": amount
                         }
                })

def act_call():
    return json.dumps({
                       "eventName": "__action",
                       "data": {
                                "action": "call",
                                }
                       })
    
def act_check():
    return json.dumps({
                       "eventName": "__action",
                       "data": {
                                "action": "check",
                                }
                       })
    
def act_fold():
    return json.dumps({
                       "eventName": "__action",
                       "data": {
                                "action": "fold",
                                }
                       })
    
def act_raise():
    return json.dumps({
                       "eventName": "__action",
                       "data": {
                                "action": "raise",
                                }
                       })
    
def act_allin():
    return json.dumps({
                       "eventName": "__action",
                       "data": {
                                "action": "allin",
                                }
                       })

def act_reload():
    return json.dumps({
                        "eventName": "__reload"
                        })
