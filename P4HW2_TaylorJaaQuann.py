# JaaQuann Taylor 
# 11/9/2024
# P4HW2
# The program calculates gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

# Pseudocode:
# 1. Initialize counters and accumulators for:
#    - Total number of employees
#    - Total overtime pay
#    - Total regular pay
#    - Total gross pay
# 2. Loop to collect employee data:
#    a. Ask for employee name or "Done" to stop.
#    b. If name is "Done", break out of the loop.
#    c. Ask for hours worked and pay rate.
#    d. Calculate overtime hours if hours worked > 40.
#    e. Calculate regular pay and overtime pay as needed.
#    f. Display individual employee's results.
# 3. After loop, display accumulated totals for:
#    - Number of employees
#    - Total overtime pay
#    - Total regular pay
#    - Total gross pay

# Initialize variables for total calculations
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Loop to collect data for each employee
while True:
    # Ask for the employee's name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break

    # Ask for hours worked and pay rate
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate overtime and regular pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = regular_hours * pay_rate
    else:
        overtime_hours = 0
        regular_hours = hours_worked
        overtime_pay = 0.0
        regular_pay = regular_hours * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Accumulate totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Display individual results for the current employee
    print("\nEmployee name: ", employee_name)
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("-" * 74)
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<14.2f} ${regular_pay:<14.2f} ${gross_pay:<10.2f}")
    print()

# Display summary of all employees
print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
