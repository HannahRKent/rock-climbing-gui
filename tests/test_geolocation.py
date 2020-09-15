import os
import unittest

from rockclimbing.geolocation import Geolocation, CountyLocationProvider, get_distance


class GeolocationTest(unittest.TestCase):

    def test_get_distance_lat_lon_km(self):
        location1 = Geolocation(1, 1)
        location2 = Geolocation(2, 2)
        distance = get_distance(location1, location2)

        self.assertAlmostEqual(distance, 157.2, 1)

    def test_get_distance_lat_lon_mi(self):
        location1 = Geolocation(1, 1)
        location2 = Geolocation(2, 2)
        distance = get_distance(location1, location2, unit="mi")

        self.assertAlmostEqual(distance, 97.7, 1)

    def test_county_location_provider(self):
        location_provider = CountyLocationProvider(os.path.join("data", "counties_geolocations.csv"))
        self.assertEqual(location_provider.get_county_location("01001"), Geolocation(32.536382, -86.64449))
        self.assertEqual(location_provider.get_county_location("42037"), Geolocation(41.045517, -76.40426))
        self.assertEqual(location_provider.get_county_location("51171"), Geolocation(38.856204, -78.573987))
        self.assertEqual(location_provider.get_county_location("00000"), None)


if __name__ == '__main__':
    unittest.main()
