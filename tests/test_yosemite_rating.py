import unittest

from rockclimbing.ratings.yosemite import Rating, parse_rating, _rating_to_number, from_number


class YosemiteRatingTest(unittest.TestCase):

    def test_parse_rating(self):
        self.assertEqual(parse_rating("5.5"), Rating.Y55)
        self.assertEqual(parse_rating("5.10"), Rating.Y510)
        self.assertEqual(parse_rating("5.10a"), Rating.Y510A)
        self.assertEqual(parse_rating("5.10a R"), Rating.Y510A)
        self.assertEqual(parse_rating("5.10a PG13"), Rating.Y510A)
        self.assertEqual(parse_rating("5.10A"), Rating.Y510A)
        self.assertEqual(parse_rating("5.10b/c"), Rating.Y510B)
        self.assertEqual(parse_rating("5.10+"), Rating.Y510)
        self.assertEqual(parse_rating("5.10-"), Rating.Y510)
        self.assertEqual(parse_rating("5.14+ R"), Rating.Y514)
        self.assertEqual(parse_rating("5.14a+ R"), Rating.Y514A)
        self.assertEqual(parse_rating("V8 5.10a/b R"), Rating.Y510A)

    def test_rating_to_number(self):
        self.assertEqual(_rating_to_number("5.1"), 1)
        self.assertEqual(_rating_to_number("5.5"), 5)
        self.assertEqual(_rating_to_number("5.10a"), 10)
        self.assertEqual(_rating_to_number("5.10b"), 10.25)

    def test_number_representation(self):
        self.assertEqual(Rating.Y51.number, 1)
        self.assertEqual(Rating.Y510A.number, 10)
        self.assertEqual(Rating.Y511.number, 11)

    def test_resolve_rating(self):
        rating = Rating(parse_rating("V8 5.10a/b R"))
        self.assertEqual(rating, Rating.Y510A)
        self.assertEqual(parse_rating("V8 5.10a/b R"), Rating.Y510A)

    def test_from_number(self):
        self.assertEqual(from_number(1), Rating.Y51)
        self.assertEqual(from_number(8.0), Rating.Y58)
        self.assertEqual(from_number(12.0), Rating.Y512A)
        self.assertEqual(from_number(13.25), Rating.Y513B)
        self.assertEqual(from_number(14.50), Rating.Y514C)
        self.assertEqual(from_number(15.75), Rating.Y515D)


if __name__ == '__main__':
    unittest.main()
