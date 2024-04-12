import csv
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            name, typing, reflection_str, year = row
            reflection = reflection_str.lower() == "yes"  # Convert to Boolean
            language = ProgrammingLanguage(name, typing, reflection, int(year))
            languages.append(language)

    for language in languages:
        print(language)

if __name__ == "__main__":
    main()
