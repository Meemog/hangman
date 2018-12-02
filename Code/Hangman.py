import random
import re

ComputerWords = ["motherboard", "hexadecimal", "python", "programming", "computer", "binary", "hexadecimal", "monitor", "image", "mouse", "keyboard", "ascii", "speakers", "compile", "headphones"]
GameMode = "0"
GameOver = False

while GameMode != "1" and GameMode != "2":
    GameMode = input("Welcome to Hangman, You have 7 lives\n\nChoose one:\n1: vs computer\n2: 2 players")

    if GameMode == "2":
        Word = input("Please enter a word")
    if GameMode == "1":
        Word = ComputerWords[random.randint(0,len(ComputerWords)-1)]

Word = Word.upper()
HiddenWord = Word
HiddenWord = list(HiddenWord)
Word = list(Word)
CheckWord = HiddenWord

for i in range(0,len(Word)):
    HiddenWord[i] = '*'
    CheckWord[i] = '*'

DisplayHiddenWord = HiddenWord
DisplayHiddenWord = "".join(DisplayHiddenWord)
print(str(DisplayHiddenWord))

GuessedLetters = []
counter = 0

while GameOver != True:
    GuessedLetter = input("Enter a letter")
    GuessedLetter = GuessedLetter.upper()

    if len(GuessedLetter) == 1:


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
                counter = counter + 1
                print("You have " + str(7 - counter) + " lives left")
            GuessedLetters.append(GuessedLetter)
    else:
        print("Please only enter 1 letter")

    DisplayHiddenWord = "".join(HiddenWord)
    print(DisplayHiddenWord)

    if counter == 7:
        print("Game Over, You loose")
        GameOver = True
    if Word == CheckWord:
        Word = "".join(Word)
        print("Congratulations, You win. The word was " + Word)
        GameOver = True


