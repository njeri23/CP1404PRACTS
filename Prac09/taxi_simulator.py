from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display available taxis."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")

def main():
    print("Let's drive!")
    bill_to_date = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    while True:
        print(f"Bill to date: ${bill_to_date:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${bill_to_date:.2f}")
            break
        elif choice == 'c':
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")
            try:
                taxi_choice = int(taxi_choice)
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    cost = current_taxi.drive(distance)
                    bill_to_date += cost
                    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                except ValueError:
                    print("Invalid distance entered")

if __name__ == "__main__":
    main()
