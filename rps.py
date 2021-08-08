from player import *
from game import *

game = Game()

player = SelfPredictingPlayer(game, 3)
player.play(game, 40)

final_score = game.get_score()
print(f"Enemy {final_score[0]} - {final_score[1]} Me")
