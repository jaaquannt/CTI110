# JaaQuann Taylor
# 11/16/2024
# P5LAB
# This program simulates a self-checkout machine, calculates change, and disperses it using the least number of bills and coins.

import random

def disperse_change(change):
    # Convert change to cents
    cents = int(round(change * 100))

    # Calculate the number of dollars
    dollars = cents // 100
    cents = cents % 100

    # The number of quarters
    quarters = cents // 25
    cents = cents % 25

    # The number of dimes
    dimes = cents // 10
    cents = cents % 10

    # The number of nickels
    nickels = cents // 5
    cents = cents % 5

    # The remaining cents, the number of pennies
    pennies = cents

    # Results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    if change == 0:
        print("No change.")

def main():
    # Random float value for the total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    # Ask user to enter the amount of money they will put into the self-checkout
    amount_given = float(input("How much cash will you put in the self-checkout? "))

    # Calculate the change
    if amount_given < total_owed:
        print("Not enough money provided. Please try again.")
        return
    change = round(amount_given - total_owed, 2)
    print(f"Change is: ${change:.2f}")

    # Disperse the change
    disperse_change(change)

# The main function
if __name__ == "__main__":
    main()
