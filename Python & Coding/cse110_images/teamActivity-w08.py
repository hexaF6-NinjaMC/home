import os
clear = lambda: os.system("cls")
clear()

var_user = int(input("How many rows and columns for the multiplication table? "))
for row in range(1, var_user + 1):
    for col in range(1, var_user + 1):
        var_space = col * row
        print(f"{var_space:5}", end=" ")
    print()