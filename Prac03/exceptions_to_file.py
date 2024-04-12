is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit the loop if an integer is successfully entered
    except ValueError:  # Catch ValueError when non-integer input is provided
        print("Please enter a valid integer.")

print("Valid result is:", result)
