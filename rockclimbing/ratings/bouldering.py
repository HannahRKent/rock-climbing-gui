import re
from enum import Enum


def parse_rating(rating):
    regex = re.compile(r"V(\d{1,2})")
    match = regex.search(rating)
    if match:
        return Rating("V{}".format(match.group(1)))
    else:
        raise RuntimeError("Could not find bouldering rating: {}".format(rating))


class Rating(Enum):
    V0 = "V0"
    V1 = "V1"
    V2 = "V2"
    V3 = "V3"
    V4 = "V4"
    V5 = "V5"
    V6 = "V6"
    V7 = "V7"
    V8 = "V8"
    V9 = "V9"
    V10 = "V10"
    V11 = "V11"
    V12 = "V12"
    V13 = "V13"
    V14 = "V14"
    V15 = "V15"
    V16 = "V16"
    V17 = "V17"

    @staticmethod
    def count():
        return 18

    def __init__(self, value):
        self.number = int(value[1:])

    def __str__(self):
        return self.value


def from_number(number):
    try:
        return Rating("V{}".format(int(number)))
    except ValueError:
        raise RuntimeError("Unable to determine Bouldering rating from '{}'".format(number))
