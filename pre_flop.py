TIGHT       = 0
MODERATE    = 1
LOOSE       = 2

#Threshold coefficient
TC2 = [
		[-50,   50], [-50,  50], [-50,  50],
        [150,   50], [ 50,  50], [  0,   0],
        [300,    0], [300,   0], [300,   0]
      ]

TC3 = [
		[ 50,   50], [ 50,  25], [ 50,  10],
		[200,   50], [200,  25], [200,  10],
		[580,    0], [580,   0], [580,   0]
	  ]

TC5 = [
		[  0,   70], [  0,  50], [  0, 30],
		[450,   50], [450,  25], [450, 10],
		[900,    0], [900,   0], [900,  0]
	  ]

#Income rate
IR2 = [
		[   7,  -351,   -334,   -314,   -318,   -308,   -264,   -217,   -166,   -113,    -53,     10,     98],
		[-279,    74,   -296,   -274,   -277,   -267,   -251,   -201,   -148,    -93,    -35,     27,    116],
		[-263,  -225,    142,   -236,   -240,   -231,   -209,   -185,   -130,    -75,    -17,     46,    134],
		[-244,  -206,   -169,    207,   -201,   -189,   -169,   -148,   -114,    -55,      2,     68,    153],
		[-247,  -208,   -171,   -138,    264,   -153,   -134,   -108,    -78,    -43,     19,     85,    154],
		[-236,  -200,   -162,   -125,    -91,    324,    -99,    -72,    -43,     -6,     37,    104,    176],
		[-192,  -182,   -143,   -108,    -75,    -43,    384,    -39,     -4,     29,     72,    120,    197],
		[-152,  -134,   -122,    -84,    -50,    -17,     16,    440,     28,     65,    106,    155,    215],
		[-104,   -86,    -69,    -56,    -19,     12,     47,     81,    499,    102,    146,    195,    254],
		[ -52,   -35,    -19,      0,     11,     46,     79,    113,    149,    549,    161,    212,    271],
		[   2,    21,     34,     55,     72,     86,    121,    153,    188,    204,    598,    228,    289],
		[  63,    79,     98,    116,    132,    151,    168,    200,    235,    249,    268,    647,    305],
		[ 146,   164,    180,    198,    198,    220,    240,    257,    291,    305,    323,    339,    704],
	  ]

IR4 = [
		[-121,  -440,   -409,   -382,   -411,   -432,   -394,   -357,   -301,   -259,   -194,   -116,     16],
		[-271,   -42,   -345,   -312,   -340,   -358,   -371,   -328,   -277,   -231,   -165,    -87,     54],
		[-245,  -183,     52,   -246,   -269, 	-287,   -300,   -308, 	-252, 	-204,   -135,    -55,     84],
		[-219,  -151,    -91, 	 152,   -200,   -211,   -227, 	-236, 	-227,   -169,   -104,    -24,    118],
		[-247,  -177, 	-113, 	 -52,    256, 	-145, 	-152, 	-158, 	-152, 	-145,    -74,      9,     99],
		[-261,  -201, 	-129, 	 -65,      3, 	 376,    -76,    -79,    -68,    -66,    -44,     48,    148],
		[-226, 	-204, 	-140, 	 -73,     -2,     66,    503,      0,     15,     24,     45,     84,    194],
		[-191, 	-166, 	-147, 	 -79,     -5,     68,    138,    647,    104,    113,    136,    177,    241],
		[-141, 	-116, 	 -91, 	 -69,     -4,     75,    150,    235,    806,    226,    255,    295,    354],
		[ -89, 	 -67,    -41, 	 -12,      7,     82,    163,    248,    349,    965,    301,    348,    410],
		[ -29, 	  -3,     22,     51,     80,    108,    185,    274,    379,    423, 	1141,    403,    473],
		[  47,    76,    101,    128,    161,    199,    230,    318,    425,    473,    529,   1325,    541],
		[ 175,   211,    237, 	 266,    249,    295,    338,    381,    491,    539,    594,    655,   1554],
	  ]

IR7 = [
		[  -6,  -462,   -422,	-397,   -459,	-495,	-469,	-433,	-383,	-336,	-274,	-188,    -39],
		[-180,    21,   -347,	-304,	-365,	-418,	-447,	-414,	-356,	-308,	-248,	-163,     -1],
		[-148,   -69,     67,   -227,	-273,	-323,	-362,	-391,	-334,	-287,	-223,	-133,     32],
		[-121,   -38,     31,    122,	-198,	-230,	-270,	-303,	-309,	-259,	-200,	-103,     64],
		[-174,   -95,	 -10,     64,	 206,	-151,	-175,	-204,	-217,	-235,	-164,	 -72,     23],
		[-208,	-135,	 -47,     35,	 108,	 298,    -87,   -106,   -112,	-128,	-124,    -26,     72],
		[-184,	-164,	 -83,      2,	  93,	 168,	 420,     -5,      6,    -10,    -10,     22,    126],
		[-146,	-128,	-111,    -26,     64,	 153,	 245,    565,	 134,    118,    118,    151,    189],
		[ -88,   -68,	 -46,	 -29,	  59,    155,	 268,	 383,	 765,    299,    305,    336,    373],
		[ -38,   -15,	   1,     30,	  51,	 147,	 256,	 377,	 536,    996,    380,    420,    462],
		[  35,    49,     72,     99,	 127,	 162,	 268,	 384,	 553,    628,   1279,    529,    574],
		[ 117,   141,	 167,	 190,	 223,    261,	 304,	 423,    591,    669,    764,   1621,    712],
		[ 269,   304,	 333,	 363,	 313,    365,	 416,    475,	 644,    720,    815,    934,   2043],
	  ]

def getThreshold(numOfPlayers, position, style):
	tc = TC2
	if numOfPlayers >= 4.5:
		tc = TC5
	elif numOfPlayers >= 2.5:
		tc = TC3

	index = 0 + style
	make1 = tc[index][0] + tc[index][1] * position
	print('make1 %d = %d + %d * %d' % (make1, tc[index][0], tc[index][1], position))
	index = 3 + style
	make2 = tc[index][0] + tc[index][1] * position
	print('make2 %d = %d + %d * %d' % (make2, tc[index][0], tc[index][1], position))
	index = 6 + style
	make4 = tc[index][0] + tc[index][1] * position
	print('make4 %d = %d + %d * %d' % (make4, tc[index][0], tc[index][1], position))
	return (make1, make2, make4)

def cardToIndex(card):
	if card[0] == 'T':
		return 8
	elif card[0] == 'J':
		return 9
	elif card[0] == 'Q':
		return 10
	elif card[0] == 'K':
		return 11
	elif card[0] == 'A':
		return 12
	else:
		return int(card[0]) - 2

def getIncomeRate(handCards, numOfPlayers):
	ir = IR2
	if numOfPlayers >= 4.5:
		ir = IR7
	elif numOfPlayers >= 2.5:
		ir = IR4

	firstIndex = cardToIndex(handCards[0])
	secondIndex = cardToIndex(handCards[1])
	if handCards[0][1] == handCards[1][1]:
		row = max(firstIndex, secondIndex)
		col = min(firstIndex, secondIndex)
	else:
		row = min(firstIndex, secondIndex)
		col = max(firstIndex, secondIndex)

	return ir[row][col]

def preFlopAction(data, style):
	if data['game']['roundName'] != 'Deal':
		raise Exception('Only for pre-flop')

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

	numOfPlayers = numGuaranteed + 0.6 * numTBD
	print('numGuaranteed = %d, numTBD = %d' % (numGuaranteed, numTBD))

	thresholds = getThreshold(numOfPlayers, numTBD, style)
	incomeRate = getIncomeRate(data['self']['cards'], numOfPlayers)
	print('Income rate = %d' % (incomeRate,))

	if incomeRate < thresholds[0]: #make1
		return 0
	elif incomeRate < thresholds[1]: #make2
		return 1
	else:                           #make4
		return 1
	
