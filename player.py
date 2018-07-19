#!/home/marvin/anaconda2/bin/python
# -*- coding:utf-8 -*-

import time, json, hashlib
import pre_flop, actions, evaluate, opponents
from table import get_table
from log_print import printAction, printDeal, printResult
from websocket import create_connection

ADDR = "ws://pokerai.trendmicro.com.cn"
#ADDR = "ws://10.64.8.72"
NAME = "76546123ad2c54af3e97b694dfac46f7"
ws = ""

m = hashlib.md5()
m.update(NAME)
my_md5 = m.hexdigest()
OPPONENTS = []

def takeAction(action, data):
    global OPPONENTS

    if action in ['__bet', '__action']:
        total_bet   = 0
        min_bet     = data['self']['minBet']
        for player in data["game"]["players"]:
            total_bet += player["bet"]
            total_bet += player["roundBet"]

        if data['game']['roundName'] == 'Deal':
            #action_result = pre_flop.preFlopAction(data, pre_flop.MODERATE)
            action_result = 1
        else:
            print OPPONENTS
            action_result = evaluate.evalAction(data, OPPONENTS)

        if action_result <=0 :
            ws.send(actions.act_check() if action == "__bet"    else actions.act_fold())
        elif action_result <= 1:
            ws.send(actions.act_call()  if action == "__action" else actions.act_bet(min_bet))
        elif action_result <= 2:
            ws.send(actions.act_raise() if action == "__action" else actions.act_bet(min_bet))
        elif action_result <= 4:
            ws.send(actions.act_raise() if action == "__action" else actions.act_bet(min_bet*2))
        elif action_result <= 8:
            ws.send(actions.act_raise() if action == "__action" else actions.act_bet(total_bet/4))
        else:
            if data['game']['roundName'] != 'River':
                ws.send(actions.act_bet(total_bet/2))
            else:
                ws.send(actions.act_bet(total_bet))

    elif action == '__show_action':
        OPPONENTS = opponents.update_opponent_action(data, OPPONENTS)
        printAction(data)
    elif action == '__deal':
        printDeal(data)
    #elif action == '__start_reload':
    #    ws.send(actions.act_reload())
    #    print '\n'
    elif action == '__round_end':
        OPPONENTS = opponents.update_opponent_threshold(data, OPPONENTS)
        printResult(data)
        print '\n'


def doListen():
    try:
        global ws
        print my_md5, "start game.....", '\n'
        ws = create_connection(ADDR)
        ws.send(json.dumps({
            "eventName": "__join",
            "data": {
                "playerName": NAME
            }
        }))
        while 1:
            result = ws.recv()
            msg = json.loads(result)
            event_name = msg['eventName']
            data = msg['data']
            takeAction(event_name, data)
    except Exception, e:
        print e.message
        doListen()


if __name__ == '__main__':
    doListen()
    
