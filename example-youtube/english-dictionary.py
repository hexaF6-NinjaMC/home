import random
import os

curDir = os.path.dirname(__file__)

word = ""
with open(f"{curDir}/engWords.txt", "r") as engWords:
    word = engWords.readlines()
    print(f"The word is: {random.choice(word)}")