import unittest
from motorcycle import Motorcycle


class TestMotorcycle(unittest.TestCase):

    def test_motorcycle(self):
        motorcycle = Motorcycle("A", "mod", 100, 50)
        self.assertEqual(motorcycle.calculate_fuel_efficiency(), 2, "Result should be 2")

        self.assertEqual(motorcycle.wheelie(), "Performing a wheelie!")


if __name__ == '__main__':
    unittest.main()
