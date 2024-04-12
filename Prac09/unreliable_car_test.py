import unittest
from unreliable_car import UnreliableCar

class TestUnreliableCar(unittest.TestCase):

    def test_drive_reliability(self):
        car = UnreliableCar("Test Car", 100, 50)  # 50% reliability
        distance_driven = car.drive(10)
        self.assertIn(distance_driven, [0, 10])  # Should either drive 10km or 0km

        car.reliability = 0  # 0% reliability
        distance_driven = car.drive(5)
        self.assertEqual(distance_driven, 0)  # Should not drive at all

        car.reliability = 100  # 100% reliability
        distance_driven = car.drive(20)
        self.assertEqual(distance_driven, 20)  # Should always drive the full distance

if __name__ == "__main__":
    unittest.main()
