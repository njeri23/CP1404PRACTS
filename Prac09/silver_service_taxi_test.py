import unittest
from silver_service_taxi import SilverServiceTaxi

class TestSilverServiceTaxi(unittest.TestCase):

    def test_get_fare(self):
        taxi = SilverServiceTaxi("Test Taxi", 100, 2.46, 2)  # Fanciness of 2
        taxi.start_fare()
        distance_driven = taxi.drive(18)
        fare = taxi.get_fare()
        self.assertEqual(distance_driven, 18)  # Should drive 18km
        self.assertAlmostEqual(fare, 48.78)  # Fare should be $48.78 (18km * $2.46/km + flagfall)

if __name__ == "__main__":
    unittest.main()
