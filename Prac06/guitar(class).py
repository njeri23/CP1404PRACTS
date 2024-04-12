class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        cost_str = "${:,.2f}".format(self.cost)
        return f"{self.name} ({self.year}) : {cost_str}"

    def get_age(self, current_year):
        """Calculate and return the age of the guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Check if the guitar is vintage (50 or more years old)."""
        age = self.get_age(current_year)
        return age >= 50
