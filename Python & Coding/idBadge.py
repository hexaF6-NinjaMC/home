"""
File: idBadge.py
Author: Aaron Bechtel

Purpose: Simulate the generation of an ID badge using inputs and various string formats.
"""

# Ask for user information to put on id badge
print()
print('Please enter the following information:')
print()
first = input('First name: ')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job = input('Job title: ')
persnum = input('ID number: ')

# extra information
hair = input('Hair color: ')
month = input('Started in month: ')
eyes = input('Eye color: ')

# boolean logic if trained:
def trained():
    trained.train_boolean = input('Training complete (y/n): ')
    if trained.train_boolean.lower() == 'y':
        return trained.train_boolean == 'yes'
    elif trained.train_boolean.lower() == 'n':
        return trained.train_boolean == 'no'
    else:
        print('Please enter a correct character (y/Y/n/N).\n')
        return trained()

trained()

# dash var is 45 (-'s)
dash = '-' * 45

# ID generation using vars above
print()
print('The ID Card is:')
# dashes (----------------)
print(dash)
print(last.upper() + ', ' + first.capitalize())
print(job.capitalize())
print('ID: ' + persnum)
print()
print(email.lower())
print(phone)
print()
print(f"{'Hair: ' + hair.capitalize():<20} Eyes: {eyes.capitalize()}")
print(f"{'Month: ' + month.capitalize():<20} Training Completed: {trained.train_boolean.capitalize()}")
# dashes (----------------)
print(dash)