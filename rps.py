from player import *
from game import *

game = Game()

player = PerfectPlayer()
player.play(game, 1000)

final_score = game.get_score()
print(f"Enemy {final_score[0]} - {final_score[1]} Me")
