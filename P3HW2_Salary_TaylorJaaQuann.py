# JaaQuann Taylor
# 10/27/2024
# P3HW2
# This program calculates an employee's salary, including regular and overtime pay, based on hours worked.

# Pseudocode:
# 1. Ask the user for the employee's name.
# 2. Ask for the number of hours worked by the employee.
# 3. Ask for the employee's pay rate.
# 4. Check if the employee worked overtime (over 40 hours). If yes, calculate overtime hours and overtime pay.
# 5. Calculate regular hours pay.
# 6. Calculate gross pay by adding regular pay and overtime pay.
# 7. Display the employee name, hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay in a formatted table.

# Ask for inputs
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Constants
regular_hours = 40
overtime_rate_multiplier = 1.5

# Calculations
if hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours * pay_rate * overtime_rate_multiplier
    regular_pay = regular_hours * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Gross pay calculation
gross_pay = regular_pay + overtime_pay

# Display results
print("-------------------------------------")
print(f"Employee name:   {employee_name}")
print("\nHours Worked   Pay Rate    OverTime   OverTime Pay     RegHour Pay     Gross Pay")
print("--------------------------------------------------------------------------------------")
print(f"{hours_worked:<12.1f}   {pay_rate:<10.1f}  {overtime_hours:<10.1f} {overtime_pay:<12.2f}     ${regular_pay:<12.2f}    ${gross_pay:<12.2f}")
