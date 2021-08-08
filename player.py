import random

game_actions = ["Rock", "Paper", "Scissors"]


# All my possible players

# Player just using randomness
class RandomPlayer():
	def play(self, game, n=1):
		for _ in range(n):
		 	print(game.play(random.choice(game_actions)))

		return


# Player that predicts itself
class SelfPredictingPlayer():
	def __init__(self, game, lookback):
		self.lookback = lookback
		self.last_moves = 0
		self.move_patterns = [0 for _ in range(3**(lookback + 1))]

		for _ in range(lookback):
			current_move = random.choice(game_actions)
			game.play(current_move)

			self.last_moves *= 3
			self.last_moves += game_actions.index(current_move)

	def choose_min(self, n):
		c = 0
		cv = self.move_patterns[n]

		for i in range(1, len(game_actions)):
			if cv > self.move_patterns[n + i]:
				c = i
				cv = self.move_patterns[n + i]
		
		return c

	def play(self, game, n=1):
		for _ in range(n):
			# Calculate next move
			self.last_moves *= 3
			self.last_moves %= 3**(self.lookback + 1)

			current_move = self.choose_min(self.last_moves)
			
			# Play it
			game.play(game_actions[current_move])

			self.last_moves += current_move
			self.move_patterns[self.last_moves] += 1

		return
