import re
from math import radians, sin, cos, acos


def get_distance_lat_long(latitude_1, longitude_1, latitude_2, longitude_2, unit="km"):
    if unit == "km":
        radius = 6371.01
    elif unit == "mi":
        radius = 3959
    else:
        raise ValueError("unit parameter should be either mi or km")

    latitude_1_radians = radians(float(latitude_1))
    longitude_1_radians = radians(float(longitude_1))
    latitude_2_radians = radians(float(latitude_2))
    longitude_2_radians = radians(float(longitude_2))

    distance = radius * acos(
        sin(latitude_1_radians) * sin(latitude_2_radians) + cos(latitude_1_radians) * cos(latitude_2_radians) * cos(
            longitude_1_radians - longitude_2_radians))

    return distance


def rating_to_number(rating, climbing_type):
    """

    :param rating:
    :param climbing_type:
    :return:
    """

    rock_regex_pattern = r"5\.(\d+).*"
    boulder_regex_pattern = r"V(\d+).*"
    offset = 0

    if "Trad" in climbing_type or "Sport" in climbing_type or "Toprope" in climbing_type:
        regex_pattern = rock_regex_pattern

    elif "Boulder" in climbing_type:
        regex_pattern = boulder_regex_pattern
        offset = 1  # since we start at V0, but we do not want our bubbles to start at magnitude 0

    else:
        return None

    regex = re.compile(regex_pattern)
    match = regex.search(rating)
    if match:
        try:
            difficulty = int(match.group(1)) + offset
        except:
            difficulty = None
        return difficulty
    else:
        return None
