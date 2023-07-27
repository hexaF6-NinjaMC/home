# Impots "time" and "os" modules to be used later.
import time
import os
# Clear() defined here.
clear = lambda: os.system('cls')

# Clear the console.
clear()
print()
# Introduces the program to the user with a greeting.
print('Hello!')
# COLOR allows the user to think of the impact of the greeting given to them with a pause, then defines itself as the COLOR.
# Each time you see this, COLOR is allowing you to think at these moments.
for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds to sink in
    time.sleep(pause_in_seconds)
print('I am the Communication Organism Living Out of Reach, or C.O.L.O.R., for short.')
print()
for pause_in_seconds in [3.5]:                
    time.sleep(pause_in_seconds)

# COLOR asks the user for their name, and stores it in the variable "name".
# COLOR proceeds to ask "name" for their favorite color ("color"), with correct formatting of spaces between words and "name".
name = input('What is your name? ')
for pause_in_seconds in [2]:
    time.sleep(pause_in_seconds)
print()
print('I have a question, ', name, '.', sep='')
for pause_in_seconds in [2]:
    time.sleep(pause_in_seconds)
# This is the favorite color question.
color = input('What is your favorite color? ')
for pause_in_seconds in [2]:
    time.sleep(pause_in_seconds)

# COLOR outputs the color in the form of a comprehensive statement with the user's name, and likes it too.
# COLOR also gives delay between each sentence to allow the user to read it, clearing midway.
print('I see that you also like the color ', color, ', ', name, '.', sep='')
for pause_in_seconds in [3]:                                                                                                                # pause for 3 seconds for dramatic effect.
    time.sleep(pause_in_seconds)
clear()                                                                                                                                     # clear the console again
print()
print('Okay, then.')
for pause_in_seconds in [1.5]:                                                                                                              # pause for 1.5 seconds
    time.sleep(pause_in_seconds)
print()
print('It was nice getting to know you, ', name, '.\nI liked learning that you loved ',color,'.', sep='')
for pause_in_seconds in [3.5]:
    time.sleep(pause_in_seconds)
print()
# COLOR is leaving the interface.
print('Goodbye for now!')
for pause_in_seconds in [2.5]:
    time.sleep(pause_in_seconds)
# Clear the console screen using clear function defined at top.
clear()
exit()                                                                                                                                     # exits the console