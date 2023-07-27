import os
clear = lambda: os.system("cls")
clear()
print()

# convert Fahrenheit scale to Celsius scale
deg_f = float(input("What is the temperature in Fahrenheit? "))
deg_c = 5 / 9 * (deg_f - 32)
print(f"The temperature in degrees Celsius is {deg_c:.1f}", chr(176), "C.", sep="")
print()

# convert Fahrenheit scale to Kelvin scale
deg_f = float(input("What is the temperature in Fahrenheit? "))
kel = 5 / 9 * (deg_f - 32) + 273.15
print(f"The temperature in Kelvin is {kel:.1f}K.")
print()

# convert Celsius scale to Fahrenheit scale
deg_c = float(input("What is the temperature in Celsius? "))
deg_f = 9 / 5 * deg_c + 32
print(f"The temperature in degrees Fahrenheit is {deg_f:.1f}", chr(176), "F.", sep="")
print()

# convert Celsius scale to Kelvin scale
deg_c = float(input("What is the temperature in Celsius? "))
kel = deg_c + 273.15
print(f"The temperature in Kelvin is {kel:.1f}K.")
print()

# convert Kelvin scale to Celsius scale
kel = float(input("What is the temperature in Kelvin? "))
deg_c = kel - 273.15
print(f"The temperature in degrees Celsius is {deg_c:.1f}", chr(176), "C.", sep="")
print()

# convert Kelvin scale to Fahrenheit scale
kel = float(input("What is the temperature in Kelvin? "))
deg_f = 9 / 5 * (kel - 273.15) + 32
print(f"The temperature in degrees Fahrenheit is {deg_f:.1f}", chr(176), "F.", sep="")
print()

exit