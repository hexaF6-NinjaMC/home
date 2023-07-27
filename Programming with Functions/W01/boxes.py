import os
clear = lambda:os.system("cls")
clear()

import math

def round_to_nearest_integer(m, u):

    # "m" is manufactured items, "u" is number items user can package per box, and "b" is total number of boxes.
    b = math.ceil(m / u)
    print(f"For {m} items, packing {u} items per box, you will need {b} boxes.")

manufactured_items = int(input("Enter the number of items manufactured: "))
package_limit = int(input("Enter the number of items you can package per box: "))
print()

round_to_nearest_integer(manufactured_items, package_limit)
print()
