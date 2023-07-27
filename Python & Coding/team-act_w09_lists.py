numbers = []
number_item = -1
while number_item != 0:
    number_item = int(input("Give a number: "))
    if number_item != 0:
        numbers.append(number_item)

sum = 0

# Sum of all values in list "numbers":
for number_in_index in numbers:
    sum += number_in_index
print(sum)

# Average of all values in list "numbers" using sum:

# Return the number (or length) "len()" of the list "numbers":
count = len(numbers)
print(count)

average = sum / count
print(average)

# Find the Maximum and Minimum values in list "numbers":
for tested_value in numbers:
    maximum_value = max(numbers)
    minimum_value = min(numbers)

print(f"Maximum: {maximum_value}")
print(f"Minimum: {minimum_value}")

print(numbers)

# Sort the list from least to greatest values:
numbers.sort()
# numbers.sort(key=myFunc)
print(numbers)
# sorted_list = numbers.sort()

