from player import *
import requests
import re

target_url = "http://www.cs.stir.ac.uk/~kms/schools/rps/index.php"

# Create a session to play in
session = requests.Session()
session.get(target_url)


# Utilities for playing the game
# Making one move
move_pattern = re.compile(r"You picked (Rock|Paper|Scissors), I picked (Rock|Paper|Scissors)\.")
def play(c):
	response = session.post(target_url, data={ "action": c })
	return move_pattern.search(response.text).groups()[1]

# The current score is displayed like <div style="font-size:40px">[score num here]</div>
score_pattern = re.compile(r"40px\"\>(\d+)\<")
def get_score():
	response = session.get(target_url)
	text_scores = score_pattern.findall(response.text)

	return (int(text_scores[0]), int(text_scores[1]))


# Play some time using the PRNG
player = SelfPredictingPlayer(play, 3)
player.play(play, 10**4)

final_score = get_score()
print(f"Enemy {final_score[0]} - {final_score[1]} Me")
