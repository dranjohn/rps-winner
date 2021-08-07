import random

game_actions = ["Rock", "Paper", "Scissors"]


# All my possible players

# Player just using randomness
class RandomPlayer():
	def play(self, n=1):
		for _ in range(n):
		 	yield random.choice(game_actions)

		return
