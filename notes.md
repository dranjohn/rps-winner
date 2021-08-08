# Rock, Paper, Scissors against an AI
I found the RPS game in [this video](https://www.youtube.com/watch?v=FDXf1XxCXAk) and wondered if I could train an AI to lose against the AI trying to predict my moves.
Playing manually worked somewhat well, my current record is 6 points advantage.
The AI got notably stronger after more rounds, so here I am now, trying to exploit it.

This entire thing is somewhat hacky:
I can only communicate with the website, so some regex is required to find the numbers I actually need.

## Attempts
### 1. Random player
This player chooses a random action each round.

Games of 1000 rounds normally end on ~350 to ~320, so the PRNG is somewhat predictable.
Best found result is 10 - 18 in 40 rounds, and I have the impression this works quite well on low round numbers.
Perfect randomness should only have a 50% on average, which isn't too good.

### 2. Self predicting player
This player attempts to predict its own move.

The self predicting player is now going to use the last $n - 1$ moves to predict its own next move.
Making $n$ moves can be described as a $n$-digit ternary number.
Let the convention be that $0$ symbolizes Rock, $1$ symbolizes Paper and $2$ symbolizes Scissors.
Then, the moves (Rock, Paper, Scissors, Paper) are describes by 0121 in ternary,
or 16 in decimal.

If a move has to be chosen, the player looks at the last $n - 1$ moves.
Let the be described by the number $l$.
Then, all possible moves result in one move set of $3 \cdot l + c$, where $c \in \{0, 1, 2\}$.
From those, choose the one which has been chosen least so far.

Last, two details to make this work:
* For the first $n - 1$ moves, choose random ones.
* When adding a move $c$, the new number $t$ represeting the last $n$ moves can be calculated from the previous one, $t'$, using $t \equiv t' \cdot 3 + c \mod 3^n$.

This player has been tested on a few $n$.
The following scores are given in the format 'enemy points - my points'.

| Lookback (n - 1) | 10 + n rounds | 100 + n rounds | 1000 + n rounds | 10000 + n rounds |
| --- | --- | --- | --- | --- |
| 1 | 5 - 2 | 32 - 35 | 332 - 334 | not tested |
| 2 | 6 - 2 | 27 - 32 | 335 - 331 | not tested |
| 3 | 6 - 3 | 40 - 23 | 281 - 247 | 2848 - 2836 |
| 4 | 6 - 2 | 43 - 24 | 331 - 249 | not tested |
| 8 | 10 - 5 | 78 - 10 | 652 - 109 | not tested |

On a low number of rounds, the game is more or less random.
Higher numbers (4 or more) do poorly, most likely due to the fact the data points get spread to thin.
The enemy then picks up on the bias towards Rock.

Feedback on the enemy move has also been implemented,
because I, for some reason, thought I'd need it.
Maybe later.

### 3. Brute-force player
This player brute-forces the first $n$ actions taken by the enemy.

This is a theoretically perfect strategy,
but the behaviour of the AI may change over time (i.e. from one day to another).
Brute-forcing from scratch takes $\mathcal{O}(n^2)$.
When an 'incorrect' move has been taken, the game _has_ to be reset.
Otherwise, the behaviour is altered for later rounds.

The current experimental runtime is around 60 seconds for 1000 rounds.
This limits this approach to about 35 rounds in 60 seconds.

This reveals a perfect strategy: Playing 2, 1, 1, 0, 0, 2, 0, 2, 2, 1, 2, 0, 1, 1, 0, 0, 2, 2, 2, 1, 2, 0, 1 followed by an infinite repitition of 1, 0, 2 wins every round.
I can't prove it, but it worked on xxxx rounds.
Playing manually in the browser reveals that a regular division by zero exception happens once the infinite pattern sets in.
