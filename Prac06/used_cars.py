from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo)

    limo.drive(115)
    print(limo)


main()
