# Found the RPS game in this video: https://www.youtube.com/watch?v=FDXf1XxCXAk

import requests
import re
import random

# Create a session to play in
session = requests.Session()
response = session.get("http://www.cs.stir.ac.uk/~kms/schools/rps/index.php")


# Utilities for playing the game
game_actions = ["Rock", "Paper", "Scissors"]

def play(c):
	session.post("http://www.cs.stir.ac.uk/~kms/schools/rps/index.php", data={ "action": c })

def play_random():
	play(random.choice(game_actions))

def get_score():
	response = session.get("http://www.cs.stir.ac.uk/~kms/schools/rps/index.php")

	# The current score is displayed like <div style="font-size:40px">[score num here]</div>
	score_pattern = re.compile(r"40px\"\>(\d+)\<")
	text_scores = score_pattern.findall(response.text)

	return (int(text_scores[0]), int(text_scores[1]))


# Play some time using the PRNG
for _ in range(10**3):
	play_random()

final_score = get_score()
print(f"Enemy {final_score[0]} - {final_score[1]} Me")

# Games normally end on ~350 to ~320, so the PRNG is somewhat predictable
