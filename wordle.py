# Made by: Shuban Pal & Hayden Chen
# Depends on: Python standard libarary and "random" module

import random

word_bank = [
    "PEACH", "SMILE", "WATER", "HOUSE", "HAPPY",
    "TABLE", "CHAIR", "MUSIC", "OCEAN", "DANCE",
    "SUNNY", "SWEET", "EARTH", "FRUIT", "RIVER",
    "DREAM", "MAGIC", "CLEAN", "QUIET", "BIRDY",
    "STONE", "SEVEN", "LEAFY", "MERRY", "TIGER",
    "HAPPY", "SUNNY", "OCEAN", "RAINY", "BEACH",
    "RIVER", "CHILD", "MAPLE", "MIRTH"
]

word = word_bank[random.randint(0, len(word_bank) - 1)]
for letter in range(1, 6):
    wordcheck = ""
    builder = ""
    inp = input("\033[1;37;40mGuess " + str(letter) + "? ")
    for j in range(len(inp)):
        iterletter = inp[j]
        if iterletter.islower():
          iterletter = iterletter.upper()
        if iterletter in word:
            if iterletter == word[j]:
                builder += str("\033[1;32;40m" + iterletter)
                wordcheck += iterletter
            else:
                builder += str("\033[1;33;40m" + iterletter)
                wordcheck += inp[j]
        else:
            builder += "\033[1;37;40m_"
            wordcheck += "_"
    print(builder)
    if wordcheck == word:
        print("\033[1;37;40mYou win!")
        break
