"""
File: bond_james-bond.py
Author: Butler Aaron Bechtel

Purpose: The bond_james-bond program asks for first name (x) and last name (y) from butler agent.
Program then displays it in the iconic, "Your name is (y), (x) (y)," format.
"""
import time
import os
clear = lambda: os.system('cls')

# Ask for name inputs here.
clear()                                                                                                                                     # clears the terminal screen
for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
    time.sleep(pause_in_seconds)
print()
print("Welcome, Agent! Let's get to know you by your name first.")
for pause_in_seconds in [4]:                                                                                                                # pause for 4 seconds
    time.sleep(pause_in_seconds)
print()
agent_first = input("What's your first name, Agent, in all CAPITAL LETTERS, please? ")                                                      # not really necessary for the request, just for demonstration.
for pause_in_seconds in [1]:                                                                                                                # pause for 1 second
    time.sleep(pause_in_seconds)
print()
agent_last = input("And what's your last name, in all CAPITAL LETTERS, please? ")                                                           # not really necessary for the request, just for demonstration.

# Display in the "y, x y" format.
clear()
print()
print("Processing...")
for pause_in_seconds in [3]:                                                                                                                # pause for 3 seconds
    time.sleep(pause_in_seconds)
output1 = "Your name is {1}, {0} {1}.".format(agent_first.capitalize(), agent_last.capitalize())                                            # format the inputs as proper names, using one format method ("FINAL TEXT").
print()
print(output1)
for pause_in_seconds in [2]:                                                                                                                # pause for 2 secondS
    time.sleep(pause_in_seconds)
print()
print(f"Welcome to the Butler Organization of Noble Deeds: B.O.N.D., Butler {agent_first.capitalize()} {agent_last.capitalize()}.")         # format the inputs as proper names, using another format method (Python 3 only) (ACTUAL FINAL TEXT).
for pause_in_seconds in [5]:                                                                                                                # pause for 5 seconds
    time.sleep(pause_in_seconds)

# Terminate the program.
clear()
exit()