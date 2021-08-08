import requests
import re

# Utilities for playing the game

# Constants
# URL the game is located at
target_url = "http://www.cs.stir.ac.uk/~kms/schools/rps/index.php"
move_pattern = re.compile(r"You picked (Rock|Paper|Scissors), I picked (Rock|Paper|Scissors)\.")
# The current score is displayed like <div style="font-size:40px">[score num here]</div>
score_pattern = re.compile(r"40px\"\>(\d+)\<")

# Represents one game session
class Game():
    def __init__(self):
        self.session = requests.session()
        self.session.get(target_url)

    def play(self, c):
        response = self.session.post(target_url, data={ "action": c })
        return move_pattern.search(response.text).groups()[1]

    def reset(self):
        self.session.post(target_url, data={ "action": "-", "reset": "Reset" })
    
    def get_score(self):
        response = self.session.get(target_url)
        text_scores = score_pattern.findall(response.text)

        return (int(text_scores[0]), int(text_scores[1]))
