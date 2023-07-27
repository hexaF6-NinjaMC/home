import os
clear = lambda:os.system("cls")
clear()

global positive_score
positive_score = 0
global negative_score
negative_score = 0
global score
score = 0

positive_questions = [1, 2, 4, 6, 7]
negative_questions = [3, 5, 8, 9, 10]

response_values = [0, 1, 2, 3]

def assign_positive_values(string):
    if string == "D":
        return 0
    elif string == "d":
        return 1
    elif string == "a":
        return 2
    elif string == "A":
        return 3
    else:
        print("Whoops!")

def assign_negative_values(string):
    if string == "D":
        return 3
    elif string == "d":
        return 2
    elif string == "a":
        return 1
    elif string == "A":
        return 0
    else:
        print("Whoops!")

def determine_score_values(question_number):
    string = input("Enter D, d, a, or A: ")
    global positive_score
    global negative_score
    global score

    if positive_questions.__contains__(question_number):
        value = assign_positive_values(string)
        positive_score += value

    elif negative_questions.__contains__(question_number):
        value = assign_negative_values(string)
        negative_score += value

    else:
        print("Whoops!")
    
def calculate_rosenberg_score():
    # global positive_score
    # global negative_score

    score = positive_score + negative_score
    print(f"\nYour score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

print("This program is an implementation of the Rosenberg Self-Esteem Scale.\nThis program will show you ten statements that\nyou could possibly\napply to yourself. Please rate how much you agree with each of the\nstatements by responding with one of these four letters:\n\nD means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.\n")

print("1. I feel that I am a person of worth, at least on an equal plane with others.")
determine_score_values(1)
print("2. I feel that I have a number of good qualities.")
determine_score_values(2)
print("3. All in all, I am inclined to feel that I am a failure.")
determine_score_values(3)
print("4. I am able to do things as well as most other people.")
determine_score_values(4)
print("5. I feel I do not have much to be proud of.")
determine_score_values(5)
print("6. I take a positive attitude toward myself.")
determine_score_values(6)
print("7. On the whole, I am satisfied with myself.")
determine_score_values(7)
print("8. I wish I could have more respect for myself.")
determine_score_values(8)
print("9. I certainly feel useless at times.")
determine_score_values(9)
print("10. At times I think I am no good at all.")
determine_score_values(10)

calculate_rosenberg_score()
