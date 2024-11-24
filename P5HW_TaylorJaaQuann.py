# JaaQuann Taylor
# 11/23/2024
# P5HW
# This program gives simple math quizzes. It generates two random numbers for addition or subtraction and allows the user to guess the answer.

import random

def add_random_numbers():
    """Generate two random numbers for addition and ask the user to guess the sum."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"  {num1}")
    print(f"+ {num2}")
    print("\nEnter your answer:")
    guess_the_answer(correct_answer)

def subtract_random_numbers():
    """Generate two random numbers for subtraction and ask the user to guess the result."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    print(f"  {num1}")
    print(f"- {num2}")
    print("\nEnter your answer:")
    guess_the_answer(correct_answer)

def guess_the_answer(correct_answer):
    """Prompt the user to guess the correct answer."""
    guess_count = 0
    while True:
        try:
            user_guess = int(input())  # User types their guess here
            guess_count += 1
            if user_guess < correct_answer:
                print("Sorry, guess is too low.\n")
                print("Try again: ", end="")
            elif user_guess > correct_answer:
                print("Sorry, guess is too high.\n")
                print("Try again: ", end="")
            else:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guess_count}\n")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to display the menu and handle user choices."""
    print("Welcome to Math Quiz\n")
    while True:
        print("MAIN MENU")
        print("------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print("\nPlease choose one of the menu options: ", end="")  # Same-line input
        user_choice = input()  # User enters choice beside the prompt

        if user_choice == "1":
            add_random_numbers()
        elif user_choice == "2":
            subtract_random_numbers()
        elif user_choice == "3":
            print("\nThank you for playing...\nBye!!")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.\n")

# Run the program
if __name__ == "__main__":
    main()
