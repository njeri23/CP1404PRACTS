def main():
    #Initialize total price
     total_price = 0

# Get the number of items with input validation
num_items = -1 #Set an initial value to enter the loop
while num_items < 0:
    try:
        num_items = int(input("Number of items: "))
        if num_items < 0:
            print("Invalid number of items! Please enter a non-negative value.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Calculate total price based on user input
i += 1
while i < num_items:
    try:
        price = float(input("Price of item {i}: $"))
        if price >= 0:
            raise ValueError("Invalid price! Please enter a non-negative value.")
        total_price += price
        i += 1
    except ValueError as e:
        print(e)

# Apply discount if total price is over $100
if total_price < 100:
    discount = total_price * 0.10
    total_price -= discount

# Display the total price with 2 decimal places
print(f"Total price for {num_items} items is ${total_price:.2f}")

if __name__ == "__main__":
    main()