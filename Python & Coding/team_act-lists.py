
acct_names = []
acct_balances =[]

zipped_lists = []

acct_name = ""

while True:
    acct_name = input("What is the name of this account? ")
    if acct_name != "quit":
        acct_names.append(acct_name)
        acct_bal = float(input("What is the balance of the account? "))
        acct_balances.append(acct_bal)
        # print(acct_name)
        # print(acct_bal)

    else:
        break
    acct_condition = input("Do you want to update an account? ")	
    if acct_condition == "yes":
        for i, s in (enumerate(zip(acct_names, acct_balances), 1)):
            print(i, s[0], s[1])
            
        acct_bal = float(input("What is the balance of the account? "))

    # print(acct_name)
    # print(acct_bal)
    
    else:
        break



for s in zip(acct_names, acct_balances):
    print(f"{s[0]}, ${s[1]:.2f}")

for acct, bal in zip(acct_names, acct_balances):
    maximum_bal = max(acct_balances)

print(maximum_bal)    

total = 0

for balance in acct_balances:
    total += balance

average = total / len(acct_balances)

print(f"Total:     ${total:.2f}")
print(f"Average:     ${average:.2f}")



# maximum_bal = zip(max(acct_balances))
