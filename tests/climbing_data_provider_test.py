import unittest

import pandas
import requests_mock

from rockclimbing.climbing_data_provider import RockClimbingDataProvider
from test_data import empty_data_frame, boulder_co_data_frame


class NoDataRockClimbingDataTest(unittest.TestCase):

    def setUp(self):
        self.rock_climbing_data = RockClimbingDataProvider(latitude=40.03, longitude=-105.25, api_key="test_key")

    def test_create_routes_data_frame_no_data(self):
        """Tests that when a json response object with no route data is passed in, it returns a single row DataFrame
        containing latitude and longitude from the original query"""
        with requests_mock.Mocker() as m:
            m.get(empty_data_frame.url, text=empty_data_frame.json_response)
            routes_df = self.rock_climbing_data.create_routes_data_frame()

        pandas.testing.assert_frame_equal(routes_df, empty_data_frame.expected_df)

    def test_create_routes_data_frame_boulder(self):
        """Tests that passing in a json response object with route returns a DataFrame, where the state column is
        populated with 'Colorado' for every value"""
        with requests_mock.Mocker() as m:
            m.get(boulder_co_data_frame.url, text=boulder_co_data_frame.json_response)
            routes_df = self.rock_climbing_data.create_routes_data_frame()

        pandas.testing.assert_series_equal(routes_df["state"], boulder_co_data_frame.expected_state_series)
