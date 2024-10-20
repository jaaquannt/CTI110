# JaaQuann Taylor
# 10/20/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules from the user
grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Calculate the lowest, highest, sum, and average of the grades
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# The letter grade based on the average
if average_grade >= 90:
    letter_grade = 'A'
elif average_grade >= 80:
    letter_grade = 'B'
elif average_grade >= 70:
    letter_grade = 'C'
elif average_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# The results
print("\n------------Results------------")
print(f"Lowest Grade:    {lowest_grade:>7.1f}")
print(f"Highest Grade:   {highest_grade:>7.1f}")
print(f"Sum of Grades:   {sum_of_grades:>8.1f}")
print(f"Average:         {average_grade:>8.2f}")
print("-------------------------------")
print(f"Your grade is: {letter_grade}")




