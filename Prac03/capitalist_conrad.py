import random

# Constants
STARTING_PRICE = 10.00
MAX_PRICE = 1000
MIN_PRICE = 0.01
INCREASE_PROBABILITY = 0.5
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
OUTPUT_FILE = "stock_prices.txt"


def main():
    price = STARTING_PRICE
    day = 0

    # Open the output file for writing
    out_file = open(OUTPUT_FILE, 'w')

    print("Starting price: ${:,.2f}".format(price))
    print("Starting price: ${:,.2f}".format(price), file=out_file)

    while MIN_PRICE < price < MAX_PRICE:
        price_change = 0
        day += 1

        # Determine whether the price increases or decreases
        if random.random() < INCREASE_PROBABILITY:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)

        # Round the price to the nearest cent
        price = round(price, 2)

        # Print and write the price for the day
        print("On day {} price is: ${:,.2f}".format(day, price))
        print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)

    # Close the output file
    out_file.close()


if __name__ == "__main__":
    main()
