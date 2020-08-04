import unittest

import pandas
import requests_mock

from climbing_data_provider import RockClimbingDataProvider
from test_data import empty_data_frame, boulder_co_data_frame


class NoDataRockClimbingDataTest(unittest.TestCase):
    def setUp(self):
        self.rock_climbing_data = RockClimbingDataProvider(latitude=40.03, longitude=-105.25, api_key="test_key")

    def test_create_routes_data_frame_no_data(self):
        with requests_mock.Mocker() as m:
            m.get(empty_data_frame.url, text=empty_data_frame.text)
            routes_dataframe = self.rock_climbing_data.create_routes_data_frame()

        pandas.testing.assert_frame_equal(routes_dataframe, empty_data_frame.expected_results)

    def test_create_routes_data_frame_boulder(self):
        with requests_mock.Mocker() as m:
            m.get(boulder_co_data_frame.url, text=boulder_co_data_frame.text)
            routes_dataframe = self.rock_climbing_data.create_routes_data_frame()

        pandas.testing.assert_series_equal(routes_dataframe["state"], boulder_co_data_frame.state_result)
