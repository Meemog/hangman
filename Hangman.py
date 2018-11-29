import random

ComputerWords = ["cat", "dog", "python", "programming", "computer", "binary", "hexadecimal", "monitor", "image", "mouse", "keyboard"]
GameMode = "0"

while GameMode != "1" and GameMode != "2":
    GameMode = input("Choose one:\n1: 2 Players\n2: vs computer")

    if GameMode == "1":
        Word = input("Please enter a word")
    if GameMode == "2":
        Word = ComputerWords[random.randint(0,len(ComputerWords))]

Word.lower
HiddenWord = list(Word)
for i in range(0, len(Word)):
    HiddenWord[i] = "_"
"".join(HiddenWord)
print(HiddenWord)