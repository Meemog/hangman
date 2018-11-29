import random
import re

ComputerWords = ["cat", "dog", "python", "programming", "computer", "binary", "hexadecimal", "monitor", "image", "mouse", "keyboard"]
GameMode = "0"
GameOver = False

while GameMode != "1" and GameMode != "2":
    GameMode = input("Choose one:\n1: vs computer\n2: 2 players")

    if GameMode == "2":
        Word = input("Please enter a word")
    if GameMode == "1":
        Word = ComputerWords[random.randint(0,len(ComputerWords))]

Word = Word.capitalize()
HiddenWord = Word
HiddenWord = list(HiddenWord)

for i in range(0,len(Word)):
    HiddenWord[i] = '_ '

HiddenWord = "".join(HiddenWord)
print(HiddenWord)

GuessedLetters = []

while GameOver != True:
    GuessedLetter = input("Enter a letter")

    if len(GuessedLetter) == 1:
        Counter = 0

        if GuessedLetter in GuessedLetters:
            print("Letter has already been chosen")

        else:
            if GuessedLetter in Word:
                print("yay")
