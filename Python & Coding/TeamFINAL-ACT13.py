import math

# Area of a square is the side squared.
# Area of a circle is pi * radius squared.
# Area of a rectangle is the side1 * side2.

def compute_rectangule_area():
    a = int(input("What is one side of the rectangle? "))
    b = int(input("What is the other side of the rectangle? "))
    area = a * b
    return area

def compute_area_circle():
    r = int(input("What is the length of the radius? "))
    area = math.pi * r ** 2
    return area

def compute_area_square():
    s = int(input("What is the length of a side? "))
    area = s ** 2
    return area

user_input = input("What is the shape? (Type QUIT to quit.) ")

while user_input.upper() != "QUIT":

    if user_input.upper() == "SQUARE":
        area = compute_area_square()
    elif user_input.upper() == "CIRCLE":
        area = compute_area_circle()
    elif user_input.upper() == "RECTANGLE":
        area = compute_rectangule_area()
    else:
        area = 0
        print("Try by entering CIRCLE, SQUARE, or RECTANGLE.")
    print(f"The area of the shape is {area}.\n")    
    user_input = input("What is the shape? (Type QUIT to quit.) ")

    




# area = compute_rectangule_area()
