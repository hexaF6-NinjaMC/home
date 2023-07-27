import os
clear = lambda:os.system("cls")
clear()

def main():
    file_reader("provinces.txt")

def file_reader(file_name):
    with open(file_name, "rt") as text_file:
        # Create a blank "provinces" list.
        provinces = []

        # Append each line to the blank "provinces" list after stripping trailing space.
        for line in text_file:
            line = line.strip()
            provinces.append(line)
        
        # Print "provinces" list.
        print(provinces)
        # length = provinces.__len__()
        # print(length)

        # Pop first and last elements of the provinces list.
        # First item removed:
        provinces.pop(0)
        #Last item removed:
        provinces.pop()
        
        for i in range(len(provinces)):
            if provinces[i] == "AB":
                provinces[i] = "Alberta"
        
        clear()
        print()
        print(provinces)

        counted = provinces.count("Alberta")
        print(f"Alberta occurs {counted} times in the modified list.")


if __name__ == "__main__":
    main()