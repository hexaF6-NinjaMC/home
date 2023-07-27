
import random

magic = random.randint(10, 100)
# magic = int(input("What is the magic number? "))

guess = int(input("Guess the number? "))
while guess != magic:
    if guess < magic:
        print("Higher")
        guess = int(input("Guess the number? "))
    elif guess > magic:
        print("Lower")
        guess = int(input("Guess the number? "))
if guess == magic:
    print("You guessed it!")
