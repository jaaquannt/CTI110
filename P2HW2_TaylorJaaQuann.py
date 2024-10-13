# JaaQuann Taylor
# 10/13/2024
# P2HW2
# This program takes input for 6 module grades, stores them in a list, and displays the lowest, highest, sum, and average grade.

# Pseudocode:
# 1. Create an empty list to store grades.
# 2. Ask the user to enter grades for 6 modules.
# 3. Calculate the lowest grade with the min() function.
# 4. Calculate the highest grade with the max() function.
# 5. Calculate the sum of grades with the sum() function.
# 6. Calculate the average by dividing the sum by the number of grades.
# 7. Display the results.

# Requesting input for module grades
grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Calculating results
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Displaying results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<20}{sum_of_grades:.1f}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("--------------------------------")
