
import os
clear = lambda:os.system("cls")
clear()

def main():
    # Get an odometer value in U.S. miles from the user.
    trip_start = int(input("Enter your odometer's previous miles traveled (before trip start): "))

    # Get another odometer value in U.S. miles from the user.
    trip_end = int(input("Enter your odometer's current miles traveled (after reaching destination): "))

    # Get a fuel amount in U.S. gallons from the user.
    used_gallons = float(input("Enter the amount of fuel used, in gallons: "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(trip_start, trip_end, used_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    rounded_mpg = round(mpg, 1)

    # Round the liters per 100 km to two digits after the decimal.
    rounded_lp100k = round(lp100k, 2)

    # Display the results for the user to see.
    print(f"Fuel efficiency in miles-per-gallon: {rounded_mpg} mpg\nFuel efficiency in liters-per-100-kilometers: {rounded_lp100k} lp100k")
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    fuel_efficiency_mpg = (end_miles - start_miles) / amount_gallons
    return fuel_efficiency_mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    fuel_efficiency_lp100k = 235.215 / mpg
    return fuel_efficiency_lp100k


# Call the main function so that
# this program will start executing.
main()