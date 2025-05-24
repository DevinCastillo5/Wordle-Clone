# Name:        Devin Castillo
# Class:       CSC 110 - Spring 2024
# Assignment:  Programming Project Design
# Due Date:    March 29, 2024

# Program Title:  Wordle

# Project Description:
# --------------------
# This program is a game that will allow the user guess a secret word by inputting a word 6 times.
# The user will receive clues after each guess, these clues will say if a certain letter is in the
# correct spot (G), somewhere in the word (Y), or not at all in the word (X). The program will also
# check if the word is in a given dictionary of words. After one round is over, the program will
# allow the user to continue or quit, continuing will keep a running score of points gained every round.

# General Solution:
# -----------------
# Draw a random word from the list of words. Allow user to guess the word 6 times, and provide clues
# after each guess. After a round, ask the user if they want to continue. Keep track of the score
# after every round.

# Pseudocode:
# -----------
# User inputs a valid file name (list of words).
# User makes a guess
#   Check if the word is inside of dictionary (take out of dictionary if used)
#       For every letter in the given word:
#           Check if letter is in the word, if so check if spot of letter is correct.
#       return string of clues
#   Else:
#       Print word is not in dictionary, and allow another attempt (does not count as attempt).
# Continue this process until there are no more turns left OR if answer is correct.
# Print score for current round, and add to overall score.
# Print overall score.
# Ask if the user wants to play again.


# Function Design:
# ----------------
import random



# Function to open and return a valid file.
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            dataFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again ... ")
    return dataFile



# Function to get the data from a file and store it inside a list.
def getData():
    dataFile = openFile()
    wordList = []

    for line in dataFile:
        line = line.strip()
        wordList.append(line)

    dataFile.close()

    return wordList



# Function to get the secret word to guess.
def getWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    worldWord = wordList[wordIndex]
    return worldWord



# Function to get a guess from user. Checks if the guess is inside
# wordList before returning it. If the word is in wordList, take it out.
def getGuess(wordList):
    goodGuess = False
    while goodGuess == False:
        guessWord = input("Make a guess: ")
        guessWord = guessWord.upper()
        if guessWord in wordList:
            goodGuess = True
        else:
            print("Word not in dictionary - try again...")
    return guessWord



# Function to run through the guessWord and see if there are any
# similarities to the worldWord. If so, add that similarity to clue.
# Uses a separate list that will mark off which letters were used.
def computeClue (guessWord, worldWord):
    clue = []

    guessList = list(guessWord)
    wordleList = list(worldWord)

    for i in range(len(guessWord)):
        if guessWord[i] == worldWord[i]:
            clue.append('G')
            guessList[i] = '$'
            wordleList[i] = '$'
        else:
            clue.append('X')

    for i in range(len(guessList)):
        if (guessList[i] in worldWord) and (guessList[i] in wordleList):
            ind = wordleList.index(guessWord[i])
            wordleList[ind] = '$'
            clue[i] = 'Y'

    clue = ''.join(clue) # TA taught me .join, I used it in order to make the list into a string
    return clue



# Function to add the round score to the overall Score and prints it.
def getOverallScore(roundScore, overallScore):
    overallScore = overallScore + roundScore
    print("Your overall score is ", overallScore)
    return overallScore



# Function to run a new round, includes a loop of guesses and clue checking.
def newRound(wordList):
    yORn = "Y"
    overallScore = 0

    while yORn == "Y":
        endRound = False
        roundScore = 0
        worldWord = getWord(wordList)
        while endRound == False:
            guessWord = getGuess(wordList)
            clue = computeClue(guessWord, worldWord)
            print(guessWord)
            print(clue)
            roundScore += 1
            if clue == "GGGGG":
                print("\nCongratulations, your wordle score for this game is ", roundScore)
                overallScore = getOverallScore(roundScore, overallScore)
                endRound = True
            elif roundScore == 6:
                print("Sorry, you did not guess the word: ", worldWord)
                roundScore = 10
                overallScore = getOverallScore(roundScore, overallScore)
                endRound = True
        yORn = input("\nWould you like to play again (Y or N)? ")
        yORn = yORn.upper()
    if yORn == "N":
        print("\nThanks for playing!")
    return



# The main function implements the pseudocode by using the functions defined above.
def main(seedValue):
    random.seed(seedValue)
    wordList = getData()
    newRound(wordList)