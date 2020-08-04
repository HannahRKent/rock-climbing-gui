import unittest

import math_utils


class MathUtilsTestCase(unittest.TestCase):

    def test_get_distance_lat_lon_km(self):
        latitude_1 = 1
        longitude_1 = 1
        latitude_2 = 2
        longitude_2 = 2

        distance = math_utils.get_distance_lat_long(latitude_1, longitude_1, latitude_2, longitude_2)

        self.assertAlmostEqual(distance, 157.2, 1)

    def test_get_distance_lat_lon_mi(self):
        latitude_1 = 1
        longitude_1 = 1
        latitude_2 = 2
        longitude_2 = 2

        distance = math_utils.get_distance_lat_long(latitude_1, longitude_1, latitude_2, longitude_2, unit="mi")

        self.assertAlmostEqual(distance, 97.7, 1)

    def test_rating_to_number_no_type(self):
        rating_number = math_utils.rating_to_number("V8", "")
        self.assertIsNone(rating_number)

    def test_rating_to_number_boulder(self):
        rating_number = math_utils.rating_to_number("V100", "123 Boulder 123")
        self.assertEqual(rating_number, 101)

    def test_rating_to_number_rock(self):
        rating_number = math_utils.rating_to_number("123 5.10a 123", "Toprope")
        self.assertEqual(rating_number, 10)


if __name__ == '__main__':
    unittest.main()
