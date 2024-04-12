import csv

def read_wimbledon_data(filename):
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            wimbledon_data.append(row)
    return wimbledon_data

def process_champions(wimbledon_data):
    champion_counts = {}
    for champion, country in wimbledon_data:
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts

def display_champions(champion_counts):
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_counts.items()):
        print(f"{champion} {count}")

def display_countries(wimbledon_data):
    countries = sorted(set(country for _, country in wimbledon_data))
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_wimbledon_data(filename)
    champion_counts = process_champions(wimbledon_data)
    display_champions(champion_counts)
    display_countries(wimbledon_data)

if __name__ == "__main__":
    main()
