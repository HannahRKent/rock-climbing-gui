import unittest

from json_helper import _build_url as build_url


class UrlConstructionTest(unittest.TestCase):
    base_url = "http://myurl.com"

    def test_build_url(self):
        result = build_url(self.base_url)
        self.assertEqual(result, self.base_url)

    def test_build_url_with_params(self):
        result = build_url(self.base_url, argument1="arg1", argument2="arg2")
        self.assertEqual(result, "http://myurl.com?argument1=arg1&argument2=arg2")


if __name__ == '__main__':
    unittest.main()
