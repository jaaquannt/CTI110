# JaaQuann Taylor
# 11/9/2024
# P4HW1
# This program collects scores, calculates the average after dropping the lowest score, and assigns a letter grade.

# Pseudocode:
# 1. Ask the user for the number of scores they want to enter.
# 2. Create an empty list to store the scores.
# 3. Use a loop to collect each score from the user:
#    a. Check if the score is between 0 and 100.
#    b. If invalid, prompt the user to enter a valid score.
#    c. If valid, add the score to the list.
# 4. Once all scores are collected:
#    a. Find the lowest score and remove it.
#    b. Calculate the average of the modified list.
#    c. Determine the letter grade based on the average.
# 5. Display the lowest score, modified list, average, and letter grade.

# Ask user for the number of scores to enter
num_scores = int(input("How many scores do you want to enter? "))

# Initialize an empty list to store scores
scores = []

# Loop to collect scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Please enter a numeric value.")

# Calculate and display results
lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
average_score = sum(modified_scores) / len(modified_scores)

# Determine letter grade
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score   : {lowest_score}")
print(f"Modified List  : {modified_scores}")
print(f"Scores Average : {average_score:.2f}")
print(f"Grade          : {grade}")
print("-------------------------------")
