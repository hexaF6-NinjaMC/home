# Purpose: demonstrate the float() and int() compatibility
# with str() output, with input in the guise of a menu price calculator.

# Rounded displays are formatted to 2 decimal place-values with code:
# print(f"[text here]: ${var_name:.2f}")

# Clear the screen
import os
clear = lambda: os.system("cls")
clear()
print()

# Menu terms input here
child = float(input("What is the price of a child's meal? "))
n_child = int(input("How many children are there? "))
adult = float(input("What is the price of an adult's meal? "))
n_adult = int(input("How many adults are there? "))
sales_tax_perc = float(input("What is the sales tax rate percentage? "))
print()

# Subtotal calculation
child_sub = child * n_child
adult_sub = adult * n_adult
sub = child_sub + adult_sub
print(f"Subtotal: ${sub:.2f}")

# Tip calculation
tip_percent = float(input("What percentage would you like to tip? "))
tip = tip_percent / 100 * sub
print(f"Tip: ${tip:.2f}")

# Sales tax calculation
sales_tax = sub * sales_tax_perc / 100
print(f"Sales tax: ${sales_tax:.2f}")

# Total calculation
total = sub + sales_tax + tip
print(f"Total: ${total:.2f}")
print()

# Transaction calculation
payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")
print()
exit