import time
import os
import statistics
clear = lambda:os.system("cls")
open_text_file = lambda:os.system("start list_of_countries.txt")
close_text_file = lambda:os.system('taskkill /IM notepad.exe /F')

clear()

# Create blank lists to append the appropriate data from the file opened below.
countries = []
years = []
life_expectancies = []
data_line = []
whole_data_table = []

# After opening file and retrieving data, close it and continue analyzing gathered data.
with open("life-expectancy.csv") as data_table:
    next(data_table)
    for line in data_table:
        line = line.strip()

        # Split all the clean data_lines and add the whole line to a list to be evaluated later.
        data_line = line.split(",")
        whole_data_table.append(data_line)

        # Separate all the pieces of data_line and add them to their appropriate list.
        countries.append(data_line[0])
        years.append(data_line[2])
        life_expectancies.append(data_line[3])

# #---------------------------------------------------------------------------------------
# # Optional: print all the data in a formatted line to the screen. (There's a lot!)
# for i, data in enumerate(zip(countries, years, life_expectancies), 1):
#     print(f"{i}. {data[0]} {data[1]} - {data[2]}")
# #---------------------------------------------------------------------------------------

print()

min_life = min(life_expectancies)
min_index = life_expectancies.index(min_life)
min_index_years = years[min_index]
min_index_countries = countries[min_index]

max_life = max(life_expectancies)
max_index = life_expectancies.index(max_life)
max_index_years = years[max_index]
max_index_countries = countries[max_index]

print(f"The maximum life was expected at {max_life} in the country {max_index_countries} during {max_index_years}.")
print(f"The minimum life was expected at {min_life} in the country {min_index_countries} during {min_index_years}.\n")

#---------------------------------------------------------------------------------------

# Find the data in the country asked of and display it.

min_year = min(years)
max_year = max(years)
countries_with_max_year = []

for sub_list in whole_data_table:
    if sub_list[2] == max_year:        
        countries_with_max_year.append(sub_list[0])

with open("list_of_countries.txt", "w+") as text_file:
    text_file.write("Enter into the terminal the country you wish to learn more about.\nYou can copy and paste the country name using Ctrl+C to copy and Ctrl+V to paste in the input line.\n")
    for i, c in enumerate(countries_with_max_year, 1):
        text_file.write(f"{i}. {c}\n")

open_text_file()

select_country_life = []
country_of_interest = input("What is the country you wish to learn more about? ")

close_text_file()

for line in whole_data_table:
        if country_of_interest.capitalize() == line[0]:
            select_country_life.append(line[3])

# Find max() and min() for the country.
max_in_country = max(select_country_life)
min_in_country = min(select_country_life)

# Convert all the ages in select_country_life to float values, then add them all together.
age = 0
for values in select_country_life:
    age += float(values)
avg_in_country = age / len(select_country_life)

# Display all the appropriate data.
print(f"For the country {country_of_interest.capitalize()}, the life expectancy data is as follows:\n   Maximum: {max_in_country}\n   Minimum: {min_in_country}\n   Average: {avg_in_country:.2f}\n")

#---------------------------------------------------------------------------------------

# Evaluate data with user input of Year
print(f"Beginning: {min_year} Ending: {max_year}\n")

year_of_interest = input("\nUsing the beginning and ending years above, type a year of interest: ")
print()

# Create a list for all the 0-based index values where the user's year_of_interest occur
correct_years_indices = []

for i in range(len(years)):
    if years[i] == year_of_interest:
        correct_years_indices.append(i)

# Create an initial total for all ages in the year of interest
age_sum = 0

year_ages = []
year_countries = []
# In this loop, the age is all the life_expectancies at the index values for the user's year_of_interest.
# Update it to get the sum of them all.
# The length of the list of indices for that year is equal to how many ages there are. If there are any mistakes or blank spaces, I think it should count them as "zeros", which would affect the total.
# Append the relevant data to their appropriate lists defined above.
for e in correct_years_indices:
    age = life_expectancies[e]
    age_sum += float(age)
    year_countries.append(countries[e])
    year_ages.append(life_expectancies[e])

# To find the average, divide the total of all the ages in the user's year by the number of times that the user's year occurs
average_life = age_sum / len(correct_years_indices)

print(f"\nThe average life expectancy in {year_of_interest} was {average_life:.2f}.")

# Calculate the max() and min() of the life_expecatncies through the chosen year, then find the corresponding data.
# Find the index at which the max() occurs in the chosen year
max_life = max(year_ages)
max_index = year_ages.index(max_life)
max_country = year_countries[max_index]

# Find the index at which the min() occurs in the chosen year
min_life = min(year_ages)
min_index = year_ages.index(min_life)
min_country = year_countries[min_index]

print(f"The maximum life expectancy during {year_of_interest} was in {max_country} with an age of {max_life}.")
print(f"The minimum life expectancy during {year_of_interest} was in {min_country} with an age of {min_life}.\n")

# This is to allow the user to record any data in a separate application before the program closes.
exit_input = input("\nPress any key to continue...")

for pause_in_seconds in [1.3]:
    time.sleep(pause_in_seconds)

clear()
# The program has completed!