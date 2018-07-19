'''
Created on Oct 12, 2017

@author: marvin_ma
'''
import os, subprocess

def _get_position(data):
    myName = data['self']['playerName']
    smallBlindName = data['game']['smallBlind']['playerName']
    players = data['game']['players']
    numOfPlayers = len(players)

    smallBlindIndex = -1
    for i in range(numOfPlayers):
        if players[i]['playerName'] == smallBlindName:
            smallBlindIndex = i
            break

    if smallBlindIndex == -1:
        raise Exception("Cannot find small blind")

    numGuaranteed = 0
    numTBD = 0
    beforeMySelf = True
    for i in range(numOfPlayers):
        index = (smallBlindIndex + i) % numOfPlayers
        player = players[index]
        if player['isSurvive'] and not player['folded']:
            if beforeMySelf:
                numGuaranteed += 1
            else:
                numTBD += 1
        if players[index]['playerName'] == myName:
            beforeMySelf = False
    return (numGuaranteed, numTBD)


def _get_table(data):
    table = {}
    ##### self info #####
    table["chips"]          = data["self"]["chips"]
    table["my_roundBet"]    = data["self"]["roundBet"]
    table["hand"]           = data["self"]["cards"]
    table["position"]       = _get_position(data)

    ##### table info #####
    table["betCount"]     = 0
    table["raiseCount"] = 0
    table["allinCount"] = 0
    table["totalBet"]   = 0
    table["players"]    = []
    table["board"]      = data["game"]["board"]
    table["roundName"]  = data["game"]["roundName"]
    table["smallBlind"] = data["game"]["smallBlind"]["amount"]
    table["bigBlind"]   = data["game"]["bigBlind"]["amount"]
    table["minBet"]     = data["self"]["minBet"]
    for player in data["game"]["players"]:
        if player["isSurvive"] == True and not player["folded"]:
            table["players"].append(player)
            if player["bet"] > table["minBet"]:
                table["raiseCount"] += 1
            if player["allIn"] == True and player["bet"] > table["minBet"]:
                table["allinCount"] += 1
            if player["bet"] > 0:
                table["betCount"] += 1
        table["totalBet"] += player["roundBet"]
    return table

def _get_winning_rate(data):
    table_data = _get_table(data)
    # hs ppot npot showdownAhead showdownTied
    hand = ''.join(table_data['hand'])
    board = ''.join(table_data['board'])
    result = os.popen('./ps-eval %s -b %s 2>/dev/null' % (hand, board)).readlines()[0].split()
    print result
    winning_rate_current  = float(result[0])
    winning_rate_positive = float(result[1])
    winning_rate_negative = float(result[2])
    winning_rate_final    = float(result[3]) + float(result[4])/2
    winning_rate_presume = (winning_rate_current+winning_rate_positive-winning_rate_negative)**(len(table_data['players'])-1)
    print('numGuaranteed = %d, numTBD = %d' % (table_data['position'][0], table_data['position'][1]))
    print("winning rate: %f * %f,  %f" % (winning_rate_current, len(table_data['players'])-1, winning_rate_presume))
    return table_data, winning_rate_final**(len(table_data['players'])-1)


def _get_threshold(table_data):
    threshold_min = 0
    threshold_hlf = 0
    threshold_one = 0
    threshold_all = 0
    return (threshold_min, threshold_hlf, threshold_one, threshold_all)


def evalAction(data, opponents):
    table_data, winning_rate = _get_winning_rate(data)
    EV = winning_rate*(table_data['totalBet']+table_data['minBet']) - (1-winning_rate)*table_data['minBet']
    print "EV: ", EV
    print "minBet: ", table_data['minBet']
    print EV/table_data['minBet']
    print "totalBet: ", table_data['totalBet']
    if EV < table_data['minBet']:
        action_result = 0
    elif EV < table_data['minBet']*2:
        action_result = 1
    elif EV < table_data['minBet']*4:
        action_result = 2
    elif EV < table_data['minBet']*8:
        action_result = 4
    elif EV < table_data['minBet']*16:
        action_result = 8
    else:
        action_result = 16

    return action_result
    

