# JaaQuann Taylor
# Date: 9/29/2024
# Assignment Name: P1HW2
# This program calculates and displays travel expenses

# Pseudocode:
# 1. Ask user to enter their travel budget.
# 2. Ask user to enter their travel destination.
# 3. Ask user how much they expect to spend on gas.
# 4. Ask user how much they expect to spend on accommodation.
# 5. Ask the user how much they expect to spend on food.
# 6. Calculate total expenses by adding gas, accommodation, and food costs.
# 7. Subtract total expenses from the budget.
# 8. Display the travel destination, initial budget, expenses, and remaining balance.

print("This program calculates and displays travel expenses")

# Step 1-2: Ask for budget and destination from the user
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

# Step 3-5: Ask for gas, accommodation, and food expenses
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("Last, how much do you need for food? "))

# Step 6-7: Calculate total expenses and remaining balance
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = budget - total_expenses

# Step 8: Display results
print(f"\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {int(budget)}")
print(f"\nFuel: {int(gas_expense)}")
print(f"Accommodation: {int(accommodation_expense)}")
print(f"Food: {int(food_expense)}")
print(f"\nRemaining Balance: {int(remaining_balance)}")

