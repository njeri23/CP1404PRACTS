"""
Emails
Estimate: 20 minutes
Actual: 22 minutes
"""

def extract_name(email):
    name = email.split("@")[0]
    name = name.replace('.', ' ')
    return name.title()

def main():
    email_dict = {}
    email = input("Email: ")
    while email:
        name = extract_name(email)
        name_correct = input(f"Is your name{name} ? (Y/n) ").strip().lower()
        if name_correct == 'n':
            name = input("Name:").strip().title()
            email_dict[email] = name
            email = input("Email: ")
    for email, name in email_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()