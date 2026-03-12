# High Score Tracker

A simple Python script to track and update high scores. This program generates a random number between **1 and 100**, compares it with the previous high score stored in a text file (`hiscore.txt`), and updates it if a new high score is achieved.

---

## Author

**Yuv Sharma**

---

## Features

* Generates a random number between **1 and 100** using Python's `random` library.
* Reads the previous high score from `hiscore.txt`.
* Updates the file if the new score is higher than the previous high score.
* Displays messages showing:

  * Previous high score
  * Current score
  * Whether the high score changed

---

## Requirements

* Python 3.x
* `random` library (built-in Python library, no installation required)

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/yuvsharma723/high-score-tracker.git
```

2. Move into the project folder

```bash
cd high-score-tracker
```

3. Run the Python script

```bash
python hiscore.py
```

---

## Example Output

### Case 1: No previous high score

```
No previous hiscore found.
The new hiscore is 75
```

### Case 2: New high score achieved

```
The previous hiscore is 62
The new hiscore is 90
```

### Case 3: High score remains unchanged

```
No change in high score
The hiscore this time is 50
The previous hiscore is 80
```

---

## Notes

* The high score is stored inside a text file called **`hiscore.txt`**.
* Each time the program runs, it generates a new random score.
* If the new score is higher than the stored score, the file is updated automatically.

---

## Learning Purpose

This project demonstrates beginner Python concepts such as:

* File handling
* Conditional statements
* Random number generation
* Basic program logic

It is a beginner-friendly project created for learning and practicing Python.

---

⭐ If you like this project, feel free to star the repository!
