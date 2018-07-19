'''
Created on 2018-07-11

@author: Masm
'''

def get_table(data):
        table["surviver"]  = 0
        table["betted"]    = 0
        table["folded"]    = 0
        table["allIn"]     = 0
        table["raiseCount"]= 0
        table["board"]     = data["game"]["board"]
        table["roundName"] = data["game"]["roundName"]
        table["bigBlind"]  = data["game"]["bigBlind"]["amount"]
        table["chips"]     = data["self"]["chips"]
        table["hand"]      = data["self"]["cards"]
        table["minBet"]    = data["self"]["minBet"] if data["self"]["minBet"] >= table["bigBlind"] else table["bigBlind"]
        for player in data["game"]["players"]:
            if player["isSurvive"] == True:
                table["surviver"] += 1
            if player["folded"] == True:
                table["folded"] += 1
            if player["allIn"] == True and player["bet"] > table["bigBlind"]:
                table["allIn"] += 1
            if player["bet"] >= 4*table["bigBlind"]:
                table["raiseCount"] += 1
            if player["bet"] > 0:
                table["betted"] += 1
        
        print("round_name: ", table["roundName"])
        print(table["betted"], "      ", table["folded"], "     ", table["raiseCount"], "   ", table["allIn"], "    ", table["surviver"])
        print("minBet/bigBlind: ", table["minBet"], "/", table["bigBlind"])
