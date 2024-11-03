# JaaQuann Taylor
# 11/3/2024
# P4LAB2
# Writing code that displays information to users using loops

run_again = "yes"
while run_again != "no":
    # Get user input
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        # Display the multiplication table
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        # Print message if the input is negative
        print("This program does not handle negative numbers.")

    # Ask the user if they want to run the program again
    run_again = input("Would you like to run the program again? ")

#If user entered "no"
print("Exiting program...")
