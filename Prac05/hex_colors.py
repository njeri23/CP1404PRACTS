def lookup_color_code(color_name):
    """
    Look up the hexadecimal code for a given color name.
    If the color name is not found, return None.
    """
    return COLOR_CODES.get(color_name.capitalize())


def main():
    # Keep looping until the user enters a blank line
    while True:
        # Prompt the user to enter a color name
        color_name = input("Enter a color name (or blank to quit): ").strip()

        # If the user entered a blank line, exit the loop
        if not color_name:
            break

        # Look up the hexadecimal code for the entered color name
        color_code = lookup_color_code(color_name)

        # If the color code was found, print it
        if color_code:
            print(f"The hexadecimal code for {color_name.capitalize()} is {color_code}.")
        else:
            print("Invalid color name. Please try again.")


if __name__ == "__main__":
    main()