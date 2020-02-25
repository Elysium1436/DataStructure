




class Card:
	"""
	Class that represents a card

	Enter a char representing the first letter of a suit, and an int from 0 to 13

	"""
	_SUITS='cdhs'
	_SUITSNAME=["Clubs", "Diamonds", "Hearts", "Spades"]
	_RANKSNAME=["Ace","Two", "Three", "Four", "Five", "Six", 
			"Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
	_RANKS=list(range(1,14))



	def __init__(self, suit, rank):
		self.rank_num=self._RANKS.index(rank)
		self.suit_char=suit

	def getsuitName(self):
		return self._SUITSNAME[self._SUITS.index(self.suit_char)]

	def getrankName(self):
		return self._RANKSNAME[self.rank_num]

	def getrankNumber(self):
		return self.rank_num

	def getsuitNameChar(self):
		return self.suit_char

	def __str__(self):
		return self.getrankName() + " of " + self.getsuitName()




car=Card('s',1)
print(car)