# Question 1
user_name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(user_name)

# Question 2
with open('name.txt', 'r') as file:
    stored_name = file.read().strip()  # Remove leading/trailing whitespace
print(f"Your name is {stored_name}")

# Question 3
with open('numbers.txt', 'r') as file:
    numbers = [int(line) for line in file.readlines()[:2]]  # Read first two lines and convert to integers
total = sum(numbers)
print(f"The total of the first two numbers is: {total}")

# Question 4
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())  # Convert each line to integer and sum
print(f"The total of all numbers is: {total}")
