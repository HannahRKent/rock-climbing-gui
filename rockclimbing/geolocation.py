from dataclasses import dataclass
from math import radians, sin, cos, acos

import pandas as pd


@dataclass
class Geolocation:
    latitude: float
    longitude: float


class CountyLocationProvider:
    def __init__(self, data_csv):
        _county_location_df = pd.read_csv(
            data_csv, dtype={"fips": str, "latitude": float, "longitude": float})
        _county_location_df.drop(columns=["state_code", "name"], inplace=True)
        self._fips_to_location = _county_location_df.set_index("fips").T.to_dict("list")

    def get_county_location(self, fips):
        lat_lon = self._fips_to_location.get(fips)
        return Geolocation(lat_lon[0], lat_lon[1]) if lat_lon else None


def get_distance(location1, location2, unit="km"):
    """
    Get the distance between two points on a map.
    :param location1: The geolocation of the first point
    :param location2: The geolocation of the second point
    :param unit: The unit the distance should be returned in.  Options: km or mi
    :return: The distance between the two points
    """
    if unit == "km":
        radius = 6371.01
    elif unit == "mi":
        radius = 3959
    else:
        raise ValueError("unit parameter should be either mi or km")

    latitude_1_radians = radians(location1.latitude)
    longitude_1_radians = radians(location1.longitude)
    latitude_2_radians = radians(location2.latitude)
    longitude_2_radians = radians(location2.longitude)

    distance = radius * acos(
        sin(latitude_1_radians) * sin(latitude_2_radians) + cos(latitude_1_radians) * cos(latitude_2_radians) * cos(
            longitude_1_radians - longitude_2_radians))

    return distance
