# Purpose: Calculate velocity of a given object.

import math
import os
import time
clear = lambda: os.system("cls")
clear()

mass = float(input("Mass (in kg): "))

# Define function name_gravity here.
def name_gravity():
    # Local variable "gravity" defined by using function_name.[variable_name], float retrieved from user input
    name_gravity.gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))

# Call function "name_gravity"
name_gravity()

# Condition of 3 possibilities: 9.8, 24, or otherwise, in floats, and must repeat if necessary.

# Set global variable "grav" = local variable "name_gravity.gravity"; break if conditions met
while name_gravity.gravity == name_gravity.gravity:
    if name_gravity.gravity == 9.8:
        grav = name_gravity.gravity
        break
    elif name_gravity.gravity == 24:
        grav = name_gravity.gravity
        break
    # Return to input for name_gravity().
    else:
        print("Please try again.\n")
        name_gravity()

sec = float(input("Time (in seconds): "))

# Define function density_liquid here.
def density_liquid():
    # Local variable "density" defined by using function_name.[variable_name], float retrieved from user input
    density_liquid.density = float(input("Density of the gas/fluid (in kg/m^3, 1.3 for air, 1000 for water): "))

# Call function "density_liquid"
density_liquid()

# Set global variable "dense" = local variable "density_liquid.density"; break if conditions met
while density_liquid.density == density_liquid.density:
    if density_liquid.density == 1.3:
        dense = density_liquid.density
        break
    elif density_liquid.density == 1000:
        dense = density_liquid.density
        break
    # Return to input for density_liquid().
    else:
        print("Please try again.\n")
        density_liquid()

# Cross-sectional area (length x width: quadrilateral; pi x r^2 for circle)
cross_area = float(input("Cross-sectional area (in m^2): "))

# Drag constant
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()

# Calculate value of lowercase "c":
c = 1/2 * dense * cross_area * drag_constant
print(f"The inner value of c is: {c:.3f}")

# Calculate and display velocities to 3 decimal spaces:
velocity_at_time_t = math.sqrt(mass * grav / c) * (1 - math.exp((-1 * math.sqrt(mass * grav * c) / mass) * sec))
print("The velocity after " + str(sec) + f" seconds is: {velocity_at_time_t:.3f} m/s\n")
# print("The velocity after " + str(time) + " seconds is: " + str(velocity_at_time_t) + " m/s\n")

v_terminal = math.sqrt(mass * grav / c)
print(f"Terminal velocity is reached at: {v_terminal:.3f} m/s\n")
# print("Terminal velocity is reached at: " + str(v_terminal) + " m/s\n")

# pause for 10 seconds
for pause_in_seconds in [10]:
    time.sleep(pause_in_seconds)

exit