"""
Iterate through the "students.csv" file while it is open
by skipping the first line and adding the data to a dictionary.
Student I-numbers are keys, and their names are corresponding values.
"""

import os
clear = lambda:os.system("cls")
clear()


def main():
    I_NUMBER = input("Please enter an I-number (xxxxxxxxx): ")

    students = read_dict("students.csv", I_NUMBER)

    if I_NUMBER not in students:
        print("No such student")
    elif len(I_NUMBER) < 9:
        print("Invalid I-number: too few digits")
    elif len(I_NUMBER) > 9:
        print("Invalid I-number: too many digits")
    elif students[I_NUMBER]:
        name = students[I_NUMBER]
        print(name)

def read_dict(file_name, I_NUMBER):
    # Create a blank dictionary
    students = {}

    # Open the data file.
    with open(file_name, "rt") as file:
        # Skip the first line of the file.
        next(file)
        for data_line in file:
            clean_line = data_line.strip()
            clean_line = clean_line.split(sep=",")
            clean_line_key = clean_line[0].replace("'", "")
            clean_line_value = clean_line[1].replace("'", "")
            students[clean_line_key] = clean_line_value

    return students


if __name__ == "__main__":
    main()
