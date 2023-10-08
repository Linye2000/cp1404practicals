"""
CP1404/CP5632 Practical
Starter code for cumulative total income program

Accountant Annie wants you to write a program to calculate the monthly cumulative totals for incomes.
The program should ask for the number of monthly incomes to enter, then get and store the incomes in a list.
When the incomes have been entered, the program should display a list of the month's income with cumulative totals.
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))
    #"num_months" mains "This variable stores the... number of months"

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes, num_months)

def print_report(incomes, num_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}    Total: ${total:10.2f}")


main()