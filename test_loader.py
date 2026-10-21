import unittest
from loader import *


class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        # my code here (hooray)
        geolocator = get_geolocator()

        locations = [
            "Museum of Modern Art",
            "USS Alabama Battleship Memorial Park"
        ]

        for loc in locations:
            result = fetch_location_data(geolocator, loc)

            self.assertIsNotNone(result)
            self.assertEqual(result["location"], loc)
            self.assertIsNotNone(result["latitude"])
            self.assertIsNotNone(result["longitude"])
            self.assertIsNotNone(result["type"])

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertIsNone(result["latitude"])
        self.assertIsNone(result["longitude"])
        self.assertIsNone(result['type'])


if __name__ == "__main__":
    unittest.main()
