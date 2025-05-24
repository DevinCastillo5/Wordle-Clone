# Wordle Clone

## Description
This project consists of a text-based Wordle clone built in Python, where users try to guess a random five-letter word within five attempts. The program selects a random word from a CSV file containing a list of five-letter words, using Python’s `random` module and seeded values to ensure fair selection.

The game gives the player feedback after each guess:
- A **G** indicates a correct letter in the correct position (green).
- A **Y** indicates a correct letter in the wrong position (yellow).
- An **X** marks letters that are not in the word (grey).

All positions start as **X** to show grey and update dynamically based on the user’s input. The project makes use of multiple Python functions and search algorithms to handle word validation, position checking, and result formatting, creating an interactive and engaging experience entirely in the terminal.

With this program, users can:
- Enter guesses and receive real-time feedback  
- See per-letter position status (G, Y, X) after each attempt  
- Play against a randomized word from a curated word list  
- Improve pattern recognition and deduction skills through gameplay

## Languages and Utilities Used
- Python
- CSV file handling
- `random` module

## Software/Environment Used
- Python
  - JetBrains PyCharm IDE
- Terminal or command-line interface
