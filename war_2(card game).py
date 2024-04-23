import random
class Card:
	def	__init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return f"{self.rank or self.suit}"

class Deck:
	def __init__(self):
		self.cards = []
		for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
			for rank in range(2, 15):
				self.cards.append(Card(suit, rank))
	def shuffle(self):
		random.shuffle(self.cards)
	def rem_card(self):
		if len(self.cards) > 0:
			return self.cards.pop()
		else:
			return None

class Wargame:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()
		self.playerhand1 = []
		self.playerhand2 = []

	def dealHands(self):
		for _ in range(26):
			self.playerhand1.append(self.deck.rem_card())
			self.playerhand2.append(self.deck.rem_card())
	def p_round(self):
			p_1 = self.playerhand1.pop(0)
			p_2 = self.playerhand2.pop(0)
			print(f"Player 1 playes: {p_1}")
			print(f"Player 2 playes: {p_2}")


			if p_1.rank > p_2.rank:
				print("PLayer 1 wins the round")
			elif p_2.rank  > p_1.rank:
				print("Player 2 wins the round")
			else:
				print(" <-- It's tie! Players go to war! --> ")

	def play_game(self):
		self.dealHands()
		while len(self.playerhand1) > 0 and  len(self.playerhand2) > 0:
			self.p_round()
			input("Press Enter to Continue...  :)")
		if len(self.playerhand1) == 0:
			print("Player 2 wins!")
		else:
			print("Player 1 wins!")

if __name__  == "__main__":
	war_game = Wargame()
	war_game.play_game()

