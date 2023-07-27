import os
clear = lambda:os.system("cls")
clear()

# Wind chill formula:
# Wind Chill (ºF) (w_t) = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16),
# where T=air_temperature_in_fahrenheit and V=wind_speed in mph.

def convert_fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return c

def convert_air_celsius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f

def calculate_wind_chill_in_fahrenheit(t, v):
    w_t = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
    return w_t

def display_wind_chill_fahrenheit(t_f, v):
    # reset wind speed to 0
    v = 0
    while v < 60:
        v += 5
        w_t = calculate_wind_chill_in_fahrenheit(t_f, v)
        print(f"At temperature {t_f:.1f}°F, and wind speed {v} mph, the windchill is {w_t:.2f}°F.")

def display_wind_chill_celsius(t, t_f, v):
    # reset wind speed to 0
    v = 0
    while v < 60:
        v += 5
        w_t = calculate_wind_chill_in_fahrenheit(t_f, v)
        w_t_c = convert_fahrenheit_to_celsius(w_t)
        print(f"At temperature {t:.1f}°C, and wind speed {v} mph, the windchill is {w_t_c:.2f}°C.")

def test_temperature_validity(d_s, t, v):
    if d_s.upper() == "F":
        if t <= 50.0 and v >= 3.0:
            return True
        else:
            return False

    elif d_s.upper() == "C":
        if t <= 10.0 and v >= 3.0:
            return True
        else:
            return False

# Program Calculation and Display

wind_speed = 3

air_temperature = float(input("What is the temperature? "))
degree_scale = input("What is the temperature scale, Fahrenheit or Celsius (F/C)? ")
temperature_validity = test_temperature_validity(degree_scale, air_temperature, wind_speed)

if temperature_validity:
    if degree_scale.upper() == "F":
        air_temperature_in_fahrenheit = air_temperature
        display_wind_chill_fahrenheit(air_temperature_in_fahrenheit, wind_speed)
    elif degree_scale.upper() == "C":
        air_temperature_in_fahrenheit = convert_air_celsius_to_fahrenheit(air_temperature)
        display_wind_chill_celsius(air_temperature, air_temperature_in_fahrenheit, wind_speed)

else:
    print("The air temperature must be at or below 50.0°F (10.0°C).")
