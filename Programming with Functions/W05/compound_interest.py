"""
Compound Interest formula:
    future_value = p * (1+r/n)^(nt) + ( m * (1+r/n)^(nt) - 1 ) / (r/n),

    where:
        p is the principal (initial investment);
        r is the rate as a float less than 1, from percentage to decimal;
        n is the frequency of interest applied, e.g., annually is 1, quarterly is 4, semiannually is 2, every other month is 6, etc.;
        t is the duration of time the interest is applied, in years;
    and m is the regular monthly contribution.

If m is not done every month, divide the yearly total of contributions by 12.
"""

import time as tm
import os
clear = lambda: os.system("cls")
clear()                         # Clear the terminal window of text.

def main():
    p, r, n, t, c, b = get_user_inputs()
    if b == True:
        m = c
        print(f"Contribution: ${m:.2f} / month")
    else:
        m = convert_to_monthly(c)
        print(f"Contribution: ${c:.2f} / year")
    future_value = calculate_future_value(p, r, n, t, m)
    total_interest = calculate_total_interest(p, m, n, t, future_value)

    print(f"Future value after {t} years: ${future_value:.2f}")
    print()
    print(f"Total interest gained in {t} years: ${total_interest:.2f}")
    return

def get_user_inputs():
    valid = False
    while valid == False:
        try:
            principal = float(input("What is the inital deposit amount? $"))
            if principal < 0:
                raise ValueError    # ... restart the loop!
            rate = float(input("What is the current rate of return (as a percentage, e.g., '5%' return = '5')? ")) / 100
            if rate < 0:
                raise ValueError    # ... restart the loop!
            frequency = int(input("How many times a year does your banking institution apply interest on your account? "))
            if frequency < 0:
                raise ValueError    # ... restart the loop!
            time = float(input("How many years (can be 1.75, 7.666667, 3, etc.) would you like your account to receive interest? "))
            if time < 0:
                raise ValueError    # ... restart the loop!
            contribution = float(input("How much would you like to regularly deposit into your account? $"))
            if contribution < 0:
                raise ValueError    # ... restart the loop!
            try:
                # The following code should evaluate (eval()) string (input) "True" to the boolean True, and "False" to False...
                contribution_sum_or_split_bool = eval(input("True or False: Would you like to contribute your regular deposit every month?\n (Type 'True' for every month or 'False' for every year, case-sensitive)   "))
                # ... and if that doesn't work,...
                if not (contribution_sum_or_split_bool == True): 
                    if not (contribution_sum_or_split_bool == False):
                        raise ValueError    # ... restart the loop!
                valid = True
                return principal, rate, frequency, time, contribution, contribution_sum_or_split_bool
            except NameError:       # From the "eval() to a boolean" portion. Errors may be raised from that, which means "restart the loop".
                print("Invalid data entry: Please re-enter all data and make any corrections as needed.\nAll dollar ($) and numerical entries should be positive values in numerical formats.\n\n   Please wait approx 3 seconds...")
                tm.sleep(3)     # Pause for 3 seconds before restarting loop
                clear()
        except ValueError:       # From any of the inputs being float() or int() errors, which means "restart the loop".
            print("Invalid data entry: Please re-enter all data and make any corrections as needed.\nAll dollar ($) and numerical entries should be positive values in numerical formats.\n\n   Please wait approx 3 seconds...")
            tm.sleep(3)     # Pause for 3 seconds before restarting loop
            clear()
            

def convert_to_monthly(c):
    m = c / 12
    return m

def calculate_future_value(p, r, n, t, m):
    pwi = p*(1+(r/n))**(n*t)        # Principal with interest
    mcwi = m*((1+r/n)**(n*t) - 1) / (r/n) # Contribution (monthly) with interest
    fV = pwi + mcwi
    return fV

def calculate_total_interest(p, m, n, t, fV):
    tI = fV - p - (m*n*t)
    return tI

if __name__ == "__main__":
    main()
