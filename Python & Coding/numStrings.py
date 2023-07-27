import os
clear = lambda: os.system('cls')

clear()

# age
age = int(input("How old are you? "))
print("On your next birthday, you will be " + str(age + 1) + ".")
print()

# egg
egg_carton = int(input("How many egg cartons do you have? "))
print("You have " + str(egg_carton * 12) + " eggs.")
print()

# cookie
cookie = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
print("Each person may have " + str(int(cookie / people)) + " cookies.")