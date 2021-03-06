# -----------
# User Instructions
# 
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):	 returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#	              exactly n of. For A hand with 4 sevens 
#	              this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#	              returns their corresponding ranks as a 
#	              tuple. For example, a hand with 2 twos
#	              and 2 fours would cause this function
#	              to return (4, 2).
# card_ranks(hand) returns an ORDERED list of the ranks 
#	              in a hand (where the order goes from
#	              highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.

hand_names = ['high card', 'one pair', 'two pairs', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'straight flush']

def poker(hands):
	"Return a list of best hands: poker([hand,...]) => hand"
	return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
	"Return a list of all items equal to the max of the iterable"
	result, maxval = [], None
	key = key or (lambda x: x)
	for x in iterable:
		xval = key(x)
		if not result or xval > maxval:
			result, maxval = [x], xval
			#print result
		elif xval == maxval:
			result.append(x)
			#print result
	return result

def hand_rank(hand):
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):            # straight flush
	    return (8, max(ranks))
	elif kind(4, ranks):                           # 4 of a kind
	    return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):        # full house
	    return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):                              # flush
	    return (5, ranks)
	elif straight(ranks):                          # straight
	    return (4, max(ranks))
	elif kind(3, ranks):                           # 3 of a kind
	    return (3, kind(3, ranks), ranks)
	elif two_pair(ranks):                          # 2 pair
	    return (2, two_pair(ranks), ranks) 
	elif kind(2, ranks):                           # kind
	    return (1, kind(2, ranks), ranks)
	else:                                          # high card
	    return (0, ranks)

def card_ranks(cards):
	"Return list of the ranks, sorted with highest first"
	ranks = ['--23456789TJQKA'.index(r) for r,s in cards]    
	ranks.sort(reverse=True)
	return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def straight(ranks):
	return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
	suits = [s for r,s in hand]
	return len(set(suits)) == 1

def kind(n, ranks):
	"""Return the first rank that this hand has exactly n of.
	Return None if there is no n-of-a-kind in the hand."""
	for r in ranks:
	    if ranks.count(r) == n:    return r
	return None

def two_pair(ranks):
	"""If there are two pair, return the two ranks as a
	tuple: (highest, lowest); otherwise return None."""
	pair = kind(2, ranks)
	lopair = kind(2, list(reversed(ranks)))
	if pair and pair != lopair:
	    return (pair, lopair)
	else:
	    return None

def test():
	"Test cases for the functions in poker program"
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House

	#print sf
	#print fk
	#print fh

	#test card_rank()
#	assert card_ranks(sf) == [10, 9, 8, 7, 6]
#	assert card_ranks(fk) == [9, 9, 9, 9, 7]
#	assert card_ranks(fh) == [10, 10, 10, 7, 7]
#	
#	# test hand_rank()
#	assert hand_rank(sf) == (8, 10)
#	assert hand_rank(fk) == (7, 9, 7)
#	assert hand_rank(fh) == (6, 10, 7)
#
#	#test poker()
#	assert poker([sf, fk, fh]) == [sf]
#	assert poker([fk, fh]) == [fk]
#	assert poker([fh, fh]) == [fh, fh]
#	assert poker([sf]) == [sf]
	#assert poker([sf] + 99*[fh]) == sf

	#assert poker([sf, fh, sf]) == [sf, sf]
	assert poker([fh, sf]) == [sf]

	return 'tests pass'

#print test()
