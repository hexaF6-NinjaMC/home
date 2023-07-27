import os
clear = lambda:os.system("cls")
clear()

import random

words = ['join', 'love', 'smile', 'waffle', 'cloud', 'head']

def append_random_numbers(numbers_list, quantity = 1):
    for _ in range(quantity):
        numbers_list.append(round(random.uniform(1,100), 1))

def main():
    randnums = [16.2, 75.1, 52.3]
    randwords = []

    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)
    append_random_words(randwords, 6)
    print(randwords)

def append_random_words(words_list, quantity = 1):
    for _ in range(quantity):
        words_list.append(random.choice(words))

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
