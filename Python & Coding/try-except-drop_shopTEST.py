
import os
clear = lambda: os.system("cls")
clear()



shopping_cart = []
running_total = []

while True:
    try:
        print("\nWelcome to the Drop Shop!")
        print()
        
        # Print menu choices on each line, and ask for a choice in that menu.
        menu_choices = ["Add item", "View cart", "Remove item", "Compute total", "Quit Drop Shop"]
        for i, action in enumerate(menu_choices, 1):
            print(f"   {i}. {action}")
    
        user_choice = int(input("\nPlease enter an acton using the numbers above: "))
        clear()
    except ValueError:
        print("Try using a number from the list above.")
