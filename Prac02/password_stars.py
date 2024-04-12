def get_password_stars():
    """Function to get the password from user"""
    return input("Enter your password: ")


def print_password_stars(password):
    """Function to print asterisks based on the length of the password"""
    print("*" * len(password))


def main():
    """Main function to run the password check program"""
    password = get_password_stars()
    print_password_stars(password)


if __name__ == "__main__":
    main()
