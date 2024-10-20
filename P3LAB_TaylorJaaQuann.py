# JaaQuann Taylor
# 10/20/2024
# P3LAB
# Program calculating the most efficient number of dollars, quarters, dimes, nickels, and pennies. 

# Get input from the user
amount = float(input("Enter the amount of money as a float: $"))

# Convert amount to cents
cents = int(round(amount * 100))

# Calculate the number of dollars
dollars = cents // 100
cents = cents % 100

# Calculate the number of quarters
quarters = cents // 25
cents = cents % 25

# Calculate the number of dimes
dimes = cents // 10
cents = cents % 10

# Calculate the number of nickels
nickels = cents // 5
cents = cents % 5

# The remaining cents are the number of pennies
pennies = cents

# The results
if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(f"{pennies} Pennies")

if amount == 0:
    print("No change")
