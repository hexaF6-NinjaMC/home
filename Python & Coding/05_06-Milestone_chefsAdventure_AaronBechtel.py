import os
import time

clear = lambda: os.system("cls")
clear()

# The story - Where it all begins:
# ---------------------------------------------
# You are a soon-to-be chef, and your goal is to impress the most Irtalian of chefs in the world,
# but, you only have 3 dishes and know nothing of the chef!
# What to do?
# ---------------------------------------------

# You have 2 lives to impess the chef. Oh, boy...
# Initial (first) life == 0
lives = 0

while lives < 2:
    # spaghetti choice
    print()
    print("You are an amateur cook trying to impress the most Italian of chefs.\nYou have the options of the dishes SPAGHETTI or LASAGNA.")

    choice = input("Which one will you choose? ")
    if choice.lower() == "spaghetti":
        clear()
        print("You don't know what kind of sauce the chef likes, and you can't ask them.")
        spaghetti_choice = input("Will your spaghetti sauce be RED (tomatoes), WHITE (cream), or made with olive OIL? ")
        if spaghetti_choice.lower() == "red":
            clear()
            red_choice = input("Will your sauce be sweet (YES or NO) ? ")
            if red_choice.lower() == "yes":
                clear()
                print("This dish was disgusting. Don't make that again!")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            elif red_choice.lower() == "no":
                clear()
                print("This dish was good, but there's something better...")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            else:
                clear()
                print("Please try again, using options that are given in CAPITAL LETTERS.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
        elif spaghetti_choice.lower() == "white":
            clear()
            print("Interesting development! But how powerful should the taste-profile be?")
            white_choice = input("Will your sauce be BOLD, or smooth and SUBTLE? ")
            if white_choice.lower() == "bold":
                clear()
                print("That was a bad dish. The chef did NOT like it!")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            elif white_choice.lower() == "subtle":
                clear()
                print("The dish was amazing! Next time, see if you can do it again!")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            else:
                clear()
                print("Please try again, using options that are given in CAPITAL LETTERS.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
        elif spaghetti_choice.lower() == "oil":
            clear()
            print("They never had Mediterranean pasta of that nature before, but they sure are willing to try it!")
            oil_choice = input("Will you use poorly-made BUDGET olive oil, or true and EXPENSIVE extra-virgin olive oil? ")
            if oil_choice.lower() == "budget":
                clear()
                print("It was a good idea, but next time, don't use budget ingredients.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            elif oil_choice.lower() == "expensive":
                clear()
                print("They loved the dish! Make it again! Please!")
                print()
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            else:
                clear()
                print("Please try again, using options that are given in CAPITAL LETTERS.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
        else:
            clear()
            print("Please try again, using options that are given in CAPITAL LETTERS.")
            for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                time.sleep(pause_in_seconds)

    # lasagna choice
    elif choice.lower() == "lasagna":
        clear()
        print("You think lasagnas are hard to make. How should you prepeare the dish?")
        lasagna_choice = input("Will you make it from SCRATCH or buy it from the STORE? ")
        if lasagna_choice.lower() == "store":
            clear()
            print("Might be a bad idea... Hopefully this fact slides by the chef!")
            store_choice = input("Do you tell them (YES or NO) ? ")
            if store_choice.lower() == "yes":
                clear()
                print("SHHHHHHHHHHHHHH! Stop telling them things!")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            elif store_choice.lower() == "no":
                clear()
                print("That was a close one! Good food though.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            else:
                clear()
                print("Please try again, using options that are given in CAPITAL LETTERS.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
        elif lasagna_choice.lower() == "scratch":
            clear()
            print("Interesting decision! But how cheesy should the sauce be?")
            scratch_choice = input("Will your sauce be CHEESY, or will you WING it? ")
            if scratch_choice.lower() == "cheesy":
                clear()
                print("You made it too cheesy. Tsk tsk. Don't make it again.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            elif scratch_choice.lower() == "wing":
                clear()
                print("Wow! You have knack for this! But there is something better...")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
            else:
                clear()
                print("Please try again, using options that are given in CAPITAL LETTERS.")
                for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                    time.sleep(pause_in_seconds)
        else:
            clear()
            print("Please try again, using options that are given in CAPITAL LETTERS.")
            for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
                time.sleep(pause_in_seconds)

    # default wrong initial choice
    else:
        clear()
        print("Please try again, using options that are given in CAPITAL LETTERS.")
        for pause_in_seconds in [2]:                                                                                                                # pause for 2 seconds
            time.sleep(pause_in_seconds)
    
    # Once "lives" == 2, the game stops. Hopefully you made their day?
    lives = lives + 1