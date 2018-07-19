
def printAction(data):
    try:
        try:
            amount = data['action']['amount']
        except:
            amount = 0
        print '-----%s \t %s \t %d/%d' % (data['action']['playerName'], data['action']['action'], data['table']['totalBet'], amount)
    except Exception, e:
        print e


def printDeal(data):
    try:
        print '\n----------%s-----------' % (data['table']['roundName'])
    except Exception, e:
        print e

def printResult(data):
    try:
        print '\n----------%s-----------' % ('Result')
        boardCards = ''
        for card in data['table']['board']:
            boardCards += card

        for player in data['players']:
            if not player['isSurvive']:
                continue

            s = player['playerName'] + ':\t'
            s += '  ' + player['hand']['message']
            s += '    %d' % (player['winMoney'])
            print s
        print '---------------------------'
    except Exception, e:
        print e
