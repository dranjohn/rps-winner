# Rock, Paper, Scissors against an AI
I found the RPS game in [this video](https://www.youtube.com/watch?v=FDXf1XxCXAk) and wondered if I could train an AI to lose against the AI trying to predict my moves.
Playing manually worked somewhat well, my current record is 6 points advantage.
The AI got notably stronger after more rounds, so here I am now, trying to exploit it.

## Players
### Random player
This player chooses a random action each round.

Games of 1000 rounds normally end on ~350 to ~320, so the PRNG is somewhat predictable.
Best found result is 10 - 18 in 40 rounds, and I have the impression this works quite well on low round numbers.
Perfect randomness should only have a 50% on average, which isn't too good.
