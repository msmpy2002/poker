'''
Created on 2018-07-11

@author: Masm
'''

### strength ###
SUPER_STRONG = 5
STRONG       = 4
MODERATE     = 3
WEAK         = 2
DRAWING      = 1

### opponent move ###
FOLD  = 0
CHECK = 1
CALL  = 2
BET   = 2
RAISE = 3
BIG_RAISE = 4
ALLIN = 5

def update_opponent_action(data, opponents):
    players = data['players']
    if not opponents:
        opponents = []
        for player in players:
            opponents.append({'name': player['playerName']})

    return opponents


def update_opponent_threshold(data, opponents):
    players = data['players']
    if not opponents:
        opponents = []
        for player in players:
            opponents.append({'name': player['playerName']})
    for opponent in opponents:
        for player in data['players']:
            if opponent['name'] == player['playerName']:
                opponent['hand'] = player['cards']
                continue


    return opponents
