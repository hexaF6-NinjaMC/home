# number = float(input("Please type a positive number: "))

# while number < 0:
#     print("Sorry that is a negative number. Please try again.")
#     number = float(input("Please type a positive number: "))

# print(f"The number is {number:.0f}.")

permit_candy = ""

while permit_candy.lower() != "yes":
    permit_candy = input("May I have a piece of candy? ")

print("Thank you.")