# JaaQuann Taylor
# Date: 09/28/2024
# Assignment Name: P1HW1
# This program calculates the result of raising a number to an exponent, and performs addition and subtraction on integers entered by the user.

# Calculating Exponents
print("-----Calculating Exponents----")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

# Addition and Subtraction
print("-----Addition and Subtraction----")
starting_int = int(input("Enter a starting integer: "))
add_int = int(input("Enter an integer to add: "))
subtract_int = int(input("Enter an integer to subtract: "))
final_result = starting_int + add_int - subtract_int
print(f"\n{starting_int} + {add_int} - {subtract_int} is equal to {final_result}\n")
