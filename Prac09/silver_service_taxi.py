from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object."""

    flagfall = 4.50  # Extra charge for each new fare

    def __init__(self, name, fuel, price_per_km, fanciness):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
