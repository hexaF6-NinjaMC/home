import random
import os

def printRandWord():
    word = ""
    curDir = os.path.dirname(__file__)
    with open(f"{curDir}/engWords.json", "r") as engWords:
        word = engWords.readlines()
    # print(word)
    word_of_the_day_line = random.choice(word)
    if word_of_the_day_line.endswith('",\n'):
        word_of_the_day = word_of_the_day_line.split(',')[0]
    else:
        word_of_the_day = word_of_the_day_line
    return f"Learn a new word: {word_of_the_day}."