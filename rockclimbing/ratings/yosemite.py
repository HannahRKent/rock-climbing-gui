import re
from enum import Enum

_letter_to_number_dict = {
    "": 0,
    "a": 0,
    "b": .25,
    "c": .5,
    "d": .75
}

_number_to_letter_dict = {v: k.upper() for k, v in _letter_to_number_dict.items()}


def parse_rating(rating):
    regex = re.compile(r"5\.(\d{1,2})([abcdABCD]?)")
    match = regex.search(rating)
    if match:
        minor = match.group(1)
        letter = match.group(2).lower()
        return Rating("5.{}{}".format(minor, letter))
    else:
        raise RuntimeError("Could not find Yosemite rating: {}".format(rating))


def _rating_to_number(value):
    regex = re.compile(r"5\.(\d+)(\w?)")
    match = regex.match(value)
    if match:
        minor = float(match.group(1))
        letter = match.group(2)
        decimal = _letter_to_number_dict[letter]
        return minor + decimal
    else:
        raise RuntimeError("Unable to determine the number representation of rating {}".format(value))


class Rating(Enum):
    Y51 = "5.1"
    Y52 = "5.2"
    Y53 = "5.3"
    Y54 = "5.4"
    Y55 = "5.5"
    Y56 = "5.6"
    Y57 = "5.7"
    Y58 = "5.8"
    Y59 = "5.9"
    Y510 = "5.10"
    Y510A = "5.10a"
    Y510B = "5.10b"
    Y510C = "5.10c"
    Y510D = "5.10d"
    Y511 = "5.11"
    Y511A = "5.11a"
    Y511B = "5.11b"
    Y511C = "5.11c"
    Y511D = "5.11d"
    Y512 = "5.12"
    Y512A = "5.12a"
    Y512B = "5.12b"
    Y512C = "5.12c"
    Y512D = "5.12d"
    Y513 = "5.13"
    Y513A = "5.13a"
    Y513B = "5.13b"
    Y513C = "5.13c"
    Y513D = "5.13d"
    Y514 = "5.14"
    Y514A = "5.14a"
    Y514B = "5.14b"
    Y514C = "5.14c"
    Y514D = "5.14d"
    Y515 = "5.15"
    Y515A = "5.15a"
    Y515B = "5.15b"
    Y515C = "5.15c"
    Y515D = "5.15d"

    @staticmethod
    def count():
        return 15

    def __init__(self, value):
        self.number = _rating_to_number(value)

    def __str__(self):
        return self.value


_number_to_rating = {rating.number: rating for rating in Rating}


def from_number(number):
    try:
        return _number_to_rating[number]
    except KeyError:
        raise RuntimeError("Unable to determine Yosemite rating from '{}'".format(number))
