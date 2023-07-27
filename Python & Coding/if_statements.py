import os
clear = lambda: os.system("cls")
clear()

def first_function():
    first_function.first_number = float(input("Please enter your first number: "))

def second_function():
    second_function.second_number = float(input("Please enter your second number: "))

first_function()

second_function()

if first_function.first_number > second_function.second_number:
    print(str(first_function.first_number) + " is greater than " + str(second_function.second_number) + ".")
elif first_function.first_number < second_function.second_number:
    print(str(first_function.first_number) + " is less than " + str(second_function.second_number) + ".")
else:
    print("These numbers are equal to each other.")

animal = input("What is your favorite animal? ")

if animal.lower() == "zebra":
    print("That is my favorite animal, too!")
else:
    print("That one is not my favorite, but it was to know that you prefer a " + animal.lower() + ".")