from player import *
from game import *

game = Game()

player = BruteForcePlayer(game, 12)
player.play(game, 24)

final_score = game.get_score()
print(f"Enemy {final_score[0]} - {final_score[1]} Me")
