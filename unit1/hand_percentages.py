from poker import hand_rank
from poker import hand_names
from deal import deal

def hand_percentages(n=700*1000):
	"Sample n random hands and print a table of frequencies for each type of hand"
	counts = [0] * 9
	for i in range(n/10):
		for hand in deal(10):
			ranking = hand_rank(hand)[0]
			counts[ranking] += 1
	for i in reversed(range(9)):
		print "%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n)

#hand_percentages(100*1000)
hand_percentages()
