def main():
    subject_data = [
        ["CP1401", "Ada Lovelace", 192],
        ["CP1404", "Alan Turing", 98],
        ["CP4321", "Bill Gates", 676],
        ["CP1234", "Steve Jobs", 123]
    ]
    display_subject_details(subject_data)

def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()
