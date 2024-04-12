import csv
from guitar import Guitar

def load_guitars(filename):
    """Load guitars from CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display guitars in the list."""
    for guitar in guitars:
        print(guitar)

def sort_guitars_by_year(guitars):
    """Sort guitars in the list by year (oldest to newest)."""
    return sorted(guitars, key=lambda x: x.year)

def main():
    """Main function to load, display, and sort guitars."""
    guitars = load_guitars('guitars.csv')
    print("List of guitars:")
    display_guitars(guitars)

    sorted_guitars = sort_guitars_by_year(guitars)
    print("\nSorted list of guitars (oldest to newest):")
    display_guitars(sorted_guitars)

    # Ask user to enter new guitar details
    name = input("Enter guitar name: ")
    year = int(input("Enter year: "))
    cost = float(input("Enter cost: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

    # Write updated list of guitars back to guitars.csv
    with open('guitars.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

    print("\nNew guitar added successfully.")

if __name__ == "__main__":
    main()
