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
