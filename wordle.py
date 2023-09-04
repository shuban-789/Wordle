# Made by: Shuban Pal & Hayden Chen
# Depends on: Python standard libarary and "random" module

# Import random module
import random
# State list type word_bank to contain all 5 letter words for the wordle
word_bank = [
    "PEACH", "SMILE", "WATER", "HOUSE", "HAPPY",
    "TABLE", "CHAIR", "MUSIC", "OCEAN", "DANCE",
    "SUNNY", "SWEET", "EARTH", "FRUIT", "RIVER",
    "DREAM", "MAGIC", "CLEAN", "QUIET", "BIRDY",
    "STONE", "SEVEN", "LEAFY", "MERRY", "TIGER",
    "LUNCH", "CLOUD", "SHARK", "RAINY", "BEACH",
    "XENON", "CHILD", "MAPLE", "MIRTH"
]
# State string type word to contain a random element from list word_bank
word = word_bank[random.randint(0, len(word_bank) - 1)]
# Operate algorithm 5 times (for 5 chances)
for i in range(1, 6):
    # State empty strings, one for comparison and one for output
    wordcheck = ""
    builder = ""
    # Prompt for input
    inp = input("\033[1;37;40mGuess " + str(i) + "? ")
    # If input is not 5 letters, tell the user to make it 5 letters long
    if len(inp) != 5:
      print("Please enter a 5 letter word as your guess!")
      break
    # If user wants to leave, they must type "exit"
    if inp == "exit":
      exit()
    # Iterate through each letter in input
    for j in range(len(inp)):
        # Let variable iterletter be the letter being iterated upon
        iterletter = inp[j]
        # If it is lowercase, make it uppercase for comparison
        if iterletter.islower():
          iterletter = iterletter.upper()
        # If letter is in the exact spot as in the random word
        if iterletter == word[j]:
          # Make it green and add it to builder string
          builder += "\033[1;32;40m" + iterletter
          wordcheck += iterletter
        # If it is in the word, but not in the same spot
        elif iterletter in word:
          # Make it yellow and add it to the builder string
          builder += "\033[1;33;40m" + iterletter
          wordcheck += "_"
        # Else, just add a _ to signify it is neither in the string nor the correct position
        else:
          builder += "\033[1;37;40m_"
          wordcheck += "_"
    # Show the string
    print(builder)
    # If the words match, the player wins
    if wordcheck == word:
        print("\033[1;37;40mYou win!")
        break
