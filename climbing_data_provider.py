import pandas

import json_helper
import math_utils
from logger import logger


class RockClimbingDataProvider:
    """
    Creates a DataFrame which contains information on rock climbing routes around a particular latitude and
    longitude.
    """

    url = "https://www.mountainproject.com/data/get-routes-for-lat-lon"

    def __init__(self, latitude, longitude, api_key, max_distance=10, max_results=20, min_diff="5.1", max_diff="5.15"):
        """
        Constructor for RockClimbingDataProvider
        :param latitude: Central Latitude for query
        :param longitude: Central Latitude for query
        :param api_key: The API Key for the Query
        :param max_distance: How far out to query from the central point, in miles.
        :param max_results: Maximum number of results
        :param min_diff: Minimum difficulty
        :param max_diff: Maximum difficulty
        """
        self.latitude = latitude
        self.longitude = longitude
        self.max_distance = max_distance
        self.max_results = max_results
        self.min_diff = min_diff
        self.max_diff = max_diff
        self.api_key = api_key

    def create_routes_data_frame(self):
        """
        Creates a DataFrame containing information on the routes queried.
        """
        routes_df = pandas.DataFrame(self._get_routes())

        if routes_df.empty:
            routes_df["latitude"] = [self.latitude]
            routes_df["longitude"] = [self.longitude]
            return routes_df

        routes_df['state'] = routes_df["location"].apply(lambda x: x[0])
        routes_df['city'] = routes_df["location"].apply(lambda x: x[1])
        routes_df["distance_from_origin"] = routes_df.apply(
            lambda x: math_utils.get_distance_lat_long(
                self.latitude, self.longitude, x["latitude"], x["longitude"], unit="mi"),
            axis=1)

        routes_df["rating_number"] = routes_df.apply(
            lambda x: math_utils.rating_to_number(x["rating"], x["type"]), axis=1)

        routes_df.dropna(subset=["rating_number"], inplace=True)

        index_names = routes_df[routes_df['distance_from_origin'] > self.max_distance].index
        routes_df.drop(index_names, inplace=True)

        return routes_df

    def _get_routes(self):
        """Queries https://www.mountainproject.com/data/get-routes-for-lat-lon """
        json_response = json_helper.get_json(
            self.url, lat=self.latitude, lon=self.longitude,
            maxDistance=self.max_distance, maxResults=self.max_results,
            minDiff=self.min_diff, maxDiff=self.max_diff, key=self.api_key)

        routes = json_response["routes"]
        logger.debug("routes: {!r}".format(routes))
        return routes
