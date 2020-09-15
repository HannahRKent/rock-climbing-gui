import unittest

from rockclimbing.ratings.bouldering import Rating, parse_rating, from_number


class BoulderingRatingTest(unittest.TestCase):

    def test_normalization(self):
        self.assertEqual(parse_rating("V2"), Rating.V2)
        self.assertEqual(parse_rating("V3+"), Rating.V3)
        self.assertEqual(parse_rating("V4/5"), Rating.V4)
        self.assertEqual(parse_rating("V6 R"), Rating.V6)
        self.assertEqual(parse_rating("V10 PG13"), Rating.V10)
        self.assertEqual(parse_rating("5.10a V13 R"), Rating.V13)
        self.assertEqual(parse_rating("V17 5.10a/b R"), Rating.V17)

    def test_number_representation(self):
        self.assertEqual(Rating.V2.number, 2)
        self.assertEqual(Rating.V7.number, 7)
        self.assertEqual(Rating.V10.number, 10)

    def test_resolve_rating(self):
        self.assertEqual(parse_rating("5.10a V8 R"), Rating.V8)

    def test_from_number(self):
        self.assertEqual(from_number(0), Rating.V0)
        self.assertEqual(from_number(8.0), Rating.V8)
        self.assertEqual(from_number(17), Rating.V17)


if __name__ == '__main__':
    unittest.main()
