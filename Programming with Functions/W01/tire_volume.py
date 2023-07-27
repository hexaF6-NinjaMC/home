"""
tire_volume.py -
Using math and datetime classes, calculate tire volume from customer's specs. If customer wants to buy product with said dimensions,
get thier phone number to contact them about price options (not implemented yet).
Store all this data in a text file (volumes.txt).
"""

# Clear the terminal screen for easy readability.
import os
clear = lambda:os.system("cls")
clear()

# Import required classes for data retrieval and calculation.
import math
from datetime import datetime

# Get the date and time from the computer.
current_date_and_time = datetime.now()

# Function calculating tire volume.
def calculate_tire_volume(w, a, d):
    # v is tire volume, w is tire width in millimeters,
    # a is tire aspect ratio, d is tire diameter in inches.
    v = math.pi * w**2 * a * (w * a + 2540 * d) / 10**10
    return v

# Acquire customer's vehicle data.
print()
model = input("Enter the model of the vehicle: ")
width = float(input("Enter the width of the tire in millimeters (e.g., 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
wheel_diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))
print()

# Use received vehicle data to calculate and print to screen tire volume.
tire_volume = calculate_tire_volume(width, aspect_ratio, wheel_diameter)
print(f"The approximate volume of the tire is {tire_volume:.2f} liters.")
print()

# Open (or create) a text file called "volumes.text" and append date (year-month-day format), model, tire dimensions, and, if acquired, phone number.
# Start with a new blank line before each input session.
with open("volumes.txt", "at") as vol_file:
    print(f"\n{current_date_and_time:%Y-%m-%d}", file=vol_file)
    print(model, file=vol_file)
    print(f"{width}, {aspect_ratio}, {wheel_diameter}", file=vol_file)
        
    # Does the customer want to buy the tire?
    user_buys = input("Would you like to purchase tires with the dimensions above (Y/N)? ")

    # If user wants to buy, get their phone number to contact them later about pricing, and append that to volumes.txt
    if user_buys.lower() == "y" or user_buys.lower() == "yes":
        phone_number = input("Please enter your phone number so we may contact you about pricing (format: xxx-xxx-xxxx or xxx.xxx.xxxx): ")
        print(f"Phone: {phone_number}", file=vol_file)
