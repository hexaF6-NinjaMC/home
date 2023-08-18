import random
import os

def printRandWord():
    word = ""
    curDir = os.path.dirname(__file__)
    with open(f"{curDir}/engWords.json", "r") as engWords:
        word = engWords.readlines()
    return f"The word is: {random.choice(word)}"