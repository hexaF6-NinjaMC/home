# Week 05 Teach: Team Activity

# Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade.
# (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

# Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out.
# Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a different message to encourage them for next time.

# Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, instead create a new variable called letter and then in each block,
# set this variable to the appropriate value. Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.

import os
clear = lambda: os.system("cls")
clear()

# where it actually starts...
grade_percent = float(input("Enter grade percentage (%): "))
print()

# Assign a + or - to the letter grade, or default no sign.
if grade_percent % 10 >= 7:
    sign = "+"
elif grade_percent % 10 < 3:
    sign = "-"
else:
    sign = ""

# Assign letter grade to grade percentage.
if grade_percent >= 70:
    if grade_percent >= 90:
        grade = "A"
        if grade_percent % 10 < 3:
            sign = "-"
        else:
            sign = ""
    elif grade_percent >= 80:
        grade = "B"
    else:
        grade = "C"
else:
    if grade_percent >= 60:
        grade = "D"
    else:
        grade = "F"
        sign = ""

# print the letter grade with the appropriate sign, if applicable.
print(f"Your grade is {grade}{sign}.")

# Determine if the user has passed the course based on their grade percentage.
if grade_percent >= 70:
    print("You passed! Congratulations!")
else:
    print("Better try again. You can do it!")