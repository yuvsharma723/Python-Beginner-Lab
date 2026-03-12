# Rock-Paper-Scissors Game

**Author:** Yuv Sharma

A simple **Rock-Paper-Scissors** game in Python where a user plays against the computer. The game keeps track of the score and allows the user to play multiple rounds.

---

## Features

- User can choose how many rounds to play.
- Computer randomly selects rock, paper, or scissors.
- Score is tracked for both the user and the computer.
- Determines the winner after all rounds.
- Option to continue playing after a game ends.
- Handles invalid number input gracefully.

---

## How to Play

1. Run the Python script.
2. The game will welcome you and ask **how many times you want to play**.
3. Enter a number (integer) for the number of rounds.
4. For each round:
   - Choose between `rock`, `paper`, or `scissor`.
   - The computer randomly selects one.
   - The game announces if it's a **win, lose, or tie**.
   - Scores are updated and displayed after each round.
5. After all rounds, the game announces the overall winner:
   - If your score is higher → **You win the game!**
   - If computer score is higher → **You lose the game.**
   - If scores are equal → **The game is a tie.**
6. You can choose to **play again** or **exit the game**.

---

## Rules

- **Rock beats Scissor**
- **Paper beats Rock**
- **Scissor beats Paper**
- Any input other than `rock`, `paper`, or `scissor` counts as a loss for the user.

---

## Dependencies

- Python 3.x
- No external libraries required except `random` (built-in).

---
## Example Gameplay

welcome to rock paper scissor game
how many times you want to play : 3
please choose from rock , paper and scissor(choosing something else, result in lose) : rock
tie
computer choose : rock
your score : 0
computer score : 0
please choose from rock , paper and scissor(choosing something else, result in lose) : paper
you win
computer choose : rock
your score : 1
computer score : 0
please choose from rock , paper and scissor(choosing something else, result in lose) : scissor
you lose
computer choose : rock
your score : 1
computer score : 1
the game is tie
do you want to continue (y/n) : n
thank you for playing

## How to Run

1. Save the script as `rock_paper_scissors.py`.
2. Open terminal/command prompt.
3. Navigate to the folder containing the script.
4. Run:

```bash
python rock_paper_scissors.py
```
## **Notes**

- Input is **case-insensitive** (`Rock`, `rock`, `ROCK` are all valid).
- Invalid choices result in a loss for that round.
- The game automatically continues if the user chooses `y` after a game.
