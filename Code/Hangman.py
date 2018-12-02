import random
import re
from pygame import mixer
import time

SongFile = "Reversed_Eclipse.mp3"

mixer.init()
mixer.music.load(SongFile)
mixer.music.play(-1)

WordFile = open("ComputerWords.txt", "r")

ComputerWords = WordFile.readlines()

WordFile.close

for ComputerWord in ComputerWords:

    ComputerWord = list(ComputerWord)
    if ComputerWord[len(ComputerWord)-1] == '\n':
        del ComputerWord[len(ComputerWord)-1]

    ComputerWord = "".join(ComputerWord)

GameMode = "0"
GameOver = False

while GameMode != "1" and GameMode != "2":
    GameMode = input("Welcome to Hangman, You have 7 lives\n\nChoose one:\n1: vs computer\n2: 2 players")

    if GameMode == "2":
        WordPass = False
    if GameMode == "1":
        Word = ComputerWords[random.randint(0,len(ComputerWords)-1)]
        WordPass = True

FirstWordPass = False
while WordPass == False:
    WordPass = True

    Word = input("Please enter a word\nOnly letters and spaces allowed")
    for i in range(0, len(Word)):
        if Word[i] == "/" or Word[i].isalpha():
            FirstWordPass = True
        else:
            FirstWordPass = False

        if Word[i] == " ":
            Word = list(Word)
            Word[i] = "/"
            Word = "".join(Word)
            FirstWordPass = True

        if FirstWordPass == False:
            WordPass = False


if GameMode == "2":
    WordFile = open("ComputerWords.txt", "a")
    Word = Word.lower()
    WordFile.writelines("\n" + Word)
    WordFile.close()

Word = Word.upper()
HiddenWord = Word
HiddenWord = list(HiddenWord)
Word = list(Word)
CheckWord = HiddenWord

if GameMode == "2":
    for i in range(0,len(Word)):
        if Word[i] == "/":
            HiddenWord[i] = '/'
            CheckWord[i] = '/'
        else:
            HiddenWord[i] = '*'
            CheckWord[i] = '*'
else:
    for i in range(0,len(Word)-1):
        if Word[i] == "/":
            HiddenWord[i] = '/'
            CheckWord[i] = '/'
        else:
            HiddenWord[i] = '*'
            CheckWord[i] = '*'

DisplayHiddenWord = HiddenWord
DisplayHiddenWord = "".join(DisplayHiddenWord)
print(str(DisplayHiddenWord))

GuessedLetters = []
HitTotal = 0
Win = False

while GameOver != True:
    GuessedLetter = input("Enter a letter")
    GuessedLetter = GuessedLetter.upper()

    if len(GuessedLetter) == 1:

        if GuessedLetter[0].isalpha():

            if GuessedLetter in GuessedLetters:
                print("Letter has already been chosen")

            else:
                if GuessedLetter in Word:
                    for i in range(0, len(Word)):
                        if Word[i] == GuessedLetter:
                            HiddenWord[i] = GuessedLetter + " "
                            CheckWord[i] = GuessedLetter
                else:
                    print("That letter is not in the word")
                    HitTotal += 1
                    print("You have " + str(7 - HitTotal) + " lives left")
                GuessedLetters.append(GuessedLetter)
        else:
            print("Please only enter a letter")
    else:
        if list(GuessedLetter) == Word:
            Win = True
        else:
            print("Please only enter 1 letter")

    DisplayHiddenWord = "".join(HiddenWord)
    print(DisplayHiddenWord)

    if HitTotal == 7:
        Word = "".join(Word)
        print("Game Over, You loose. The word was " + Word)
        GameOver = True
    if Word == CheckWord:
        Win = True

    if Win == True:
        for i in range(0, len(Word)):
            if Word[i] == "/":
                Word[i] = " "

        Word = "".join(Word)
        print("Congratulations, You win. The word was " + Word)
        GameOver = True

mixer.music.fadeout(3000)
time.sleep(3)
mixer.music.stop()
