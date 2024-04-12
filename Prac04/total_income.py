def get_income_input(months_count):
    """Get income input for each month."""
    incomes = []
    for month in range(1, months_count + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes

def print_income_report(incomes):
    """Print income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Display income report for incomes over a given number of months."""
    months_count = int(input("How many months? "))
    incomes = get_income_input(months_count)
    print_income_report(incomes)

main()
