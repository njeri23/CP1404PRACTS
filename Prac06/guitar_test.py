from guitar import Guitar


def test_guitar_methods():
    """Test the get_age() and is_vintage() methods of the Guitar class."""
    current_year = 2022

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1200.50)

    assert gibson.get_age(current_year) == 100
    assert another_guitar.get_age(current_year) == 9

    assert gibson.is_vintage(current_year) == True
    assert another_guitar.is_vintage(current_year) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_guitar_methods()
