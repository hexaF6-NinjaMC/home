import os
clear = lambda:os.system("cls")
clear()

def display_regular(string):
    converted_string = string
    print(converted_string)

def display_uppercase(string):
    converted_string = string.upper()
    print(converted_string)

def display_lowercase(string):
    converted_string = string.lower()
    print(converted_string)

message = input("What is your message? ")
display_regular(message)
display_uppercase(message)
display_lowercase(message)
