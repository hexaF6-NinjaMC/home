# Purpose: demonstrate number operands and functions with input converted to integers
import os
import math
clear = lambda: os.system("cls")
clear()
print()
# float()'s are like int()'s; they must be converted to str() to be combined into the output for a print().
squared = float(input("What is the length of a side of the square? "))
print("The area of the square is: " + str(squared ** 2))
r_length = float(input("What is the length of the longest side (length) of the rectangle? "))
r_width = float(input("What is the length of the shortest side (width) of the rectangle? "))
print("The area of the rectangle is: " + str(r_length * r_width))
radius = float(input("What is the radius of the circle? "))
# 'ndigits' formats decimal into number of trailing decimal spaces, with rounding function going to the nearest value up or down, in proper procedure (0-4, down; 5-9, up).
# math.pi (called from "import math") calls the exact value of the constant pi (~3.14159).
c_area = round(float(math.pi * radius * radius), ndigits=4)

# test against what is above:
# c_area = float(math.pi * radius * radius)

print("The area of the circle is: " + str(c_area))
exit