
import time
import os
clear = lambda: os.system("cls")
clear()
print("\nWelcome to the Drop Shop!\n")

user_choice = 0

shopping_cart = []
running_total = []

while True:
    try:
        print("Drop shop - Main Menu\n")

        # Print menu choices on each line, and ask for a choice in that menu.
        menu_choices = ["Add item", "View cart", "Remove item", "Compute total", "Quit Drop Shop"]
        for i, action in enumerate(menu_choices, 1):
            print(f"   {i}. {action}")

        user_choice = int(input("\nPlease enter an action using the numbers above: "))
        clear()

        if user_choice != 5:
            while user_choice != 5:

                # Add items to cart
                if user_choice == 1:
                    print("\nAdd an item:\n")
                    item_added = input("What item would you like to add? ")
                    while True:
                        try:
                            price_of_item_added = float(input(f"What is the price of '{item_added.lower()}'? "))
                            break
                        except ValueError:
                            print("Please input the price in numerical format.")
                            clear()
                    shopping_cart.append(item_added.lower())
                    running_total.append(price_of_item_added)

                    print(f"\n'{item_added}' has successfully been added to the shopping cart.\n")
                    # pause for 3 seconds
                    for pause_in_seconds in [3]:
                        time.sleep(pause_in_seconds)
                    clear()

                    print("Drop shop - Main Menu\n")
                    for i, action in enumerate(menu_choices, 1):
                        print(f"   {i}. {action}")
                    user_choice = int(input("\nPlease enter an action using the numbers above: "))
                    clear()

                # View cart contents
                elif user_choice == 2:
                    print("\nYour Drop Shop cart contains:\n")
                    for i in range(len(shopping_cart)):
                        item = shopping_cart[i]
                        price = running_total[i]

                        print(f"{i + 1}. {item} - ${price:.2f}")
                    print()
                    print("-" * 20)
                    print()
                    print("Drop shop - Main Menu\n")
                    for i, action in enumerate(menu_choices, 1):
                        print(f"   {i}. {action}")
                    user_choice = int(input("\nPlease enter an action using the numbers above: "))
                    clear()

                # Remove items and prices from cart
                elif user_choice == 3:
                    # Lists that have values stored within them return Booleans of True,
                    # whereas empty lists return Booleans of False.

                    # Check if the shopping_cart list contains elements... (True)
                    if shopping_cart:
                        while shopping_cart:
                            
                            print("\nRemove items:\n")
                            for i, s in enumerate(zip(shopping_cart, running_total), 1):
                                print(f"    {i}. {s[0]} - ${s[1]:.2f}")
                                                                
                            try:
                                cart_item = int(input("\nWhich item number do you wish to remove? "))
                                if cart_item > 0 and cart_item <= len(shopping_cart):
                                    shopping_cart.pop(cart_item - 1)
                                    running_total.pop(cart_item - 1)
                                    clear()
                                    print(f"\nItem successfully removed.\n")
                                    print("-" * 20)
                                    break
                                else:
                                    clear()
                                    print("Try another selection using the numbered items below from your cart.")

                            except ValueError:
                                clear()
                                print("Try another selection using the numbered items below from your cart.")

                            except IndexError:
                                clear()
                                print("Try another selection using the numbered items below from your cart.")

                            except TypeError:
                                clear()
                                print("Try another selection using the numbered items below from your cart.")

                    # ...or not. (False)
                    else:
                        print("\nNothing to remove. Add items to your Drop Shop cart!\n")

                    print("Drop shop - Main Menu\n")
                    for i, action in enumerate(menu_choices, 1):
                        print(f"   {i}. {action}")
                    user_choice = int(input("\nPlease enter an action using the numbers above: "))
                    clear()

                # Compute total in cart
                elif user_choice == 4:
                    cart_total = 0
                    for price in running_total:
                        cart_total += price
                    print(f"\nThe total price of the items in your Drop Shop cart is ${cart_total:.2f}.\n")
                    print("-" * 20)
                    print("\nDrop shop - Main Menu\n")
                    for i, action in enumerate(menu_choices, 1):
                        print(f"   {i}. {action}")
                    user_choice = int(input("\nPlease enter an action using the numbers above: "))
                    clear()

                # Ask for a number, specifying in the menu list range.
                else:
                    print("\nPlease provide a number, 1 through 5.\n")
                    for i, action in enumerate(menu_choices, 1):
                        print(f"   {i}. {action}")
                    user_choice = int(input("\nPlease enter an action using the numbers above: "))
                    clear()

        # 5. Quit Drop Shop
        if user_choice == 5:
            print("Thank you for shopping the Drop Shop! Goodbye!")

            # pause for 3 seconds
            for pause_in_seconds in [3]:
                time.sleep(pause_in_seconds)
            clear()
            exit
            break

    except ValueError:
        clear()
        print("\nTry using a number from the list below.\n")