import os
clear = lambda:os.system("cls")
clear()

from datetime import datetime

# Get the current date and time.
dt = datetime.now()

# Get the day of the week using the current date and time.
dw = dt.weekday()
# dw = 4

subtotal = 0
shopping_list_prices = []
user_input = ""

while user_input.lower() != "done":
    user_input = input("Enter the item price: $")
    if user_input.lower() != "done":
        shopping_list_prices.append(float(user_input))

for item_price in shopping_list_prices:
    subtotal += item_price

discount_rate = 0.10
discount = 0

# Check if the subtotal is a Tuesday or Wednesday (2 or 3, respectively) and if the total is 50 or more dollars...
print(f"Day {dw}")
if subtotal >= 50:
    if dw == 2 or dw == 3:

        # Calculate discount amount.
        discount = round(discount_rate * subtotal, 2)

        # Convert the new subtotal from the subtotal minus the discounted savings.
        subtotal = subtotal - discount

        # Print the discounted customer's savings.
        print(f"You saved ${discount:.2f}!")
        

# Or, incentivise the customer with potential savings.
else:
    difference_to_save =  50 - subtotal
    print(f"Buy another ${difference_to_save:.2f} to save {discount_rate * 100}%!")

# Print the subtotal to the screen.
print(f"Subtotal: ${subtotal:.2f}")

# Sales tax rate can be adjusted here.
sales_tax_rate = 0.06
# Print to screen the current sales tax rate as a percentage.
print(f"Sales tax rate: {sales_tax_rate * 100:.0f}%")

# Sales tax is the dollar amount to be added to the customer's subtotal. Print the sales tax amount to the screen.
sales_tax = round(subtotal * sales_tax_rate, 2)
print(f"Sales tax: ${sales_tax:.2f}")

# Calculate the final total amount due, and print it to the screen.
total_amount_due = round(subtotal + sales_tax, 2)
print(f"\nTotal due: ${total_amount_due:.2f}")
