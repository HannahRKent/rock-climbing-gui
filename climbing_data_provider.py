import os

import pandas

import json_helper
import math_utils
from logger import logger


class RockClimbingDataProvider:
    url = "https://www.mountainproject.com/data/get-routes-for-lat-lon"

    max_distance = 10
    max_results = 20
    min_diff = "5.1"
    max_diff = "5.15"

    def __init__(self, latitude, longitude, max_distance=10, max_results=20, min_diff="5.1", max_diff="5.15",
                 api_key=os.getenv("APIKEY")):
        self.latitude = latitude
        self.longitude = longitude
        self.max_distance = max_distance
        self.max_results = max_results
        self.min_diff = min_diff
        self.max_diff = max_diff
        self.api_key = api_key

    def create_routes_data_frame(self):
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
        json_response = json_helper.get_json(
            self.url, lat=self.latitude, lon=self.longitude,
            maxDistance=self.max_distance, maxResults=self.max_results,
            minDiff=self.min_diff, maxDiff=self.max_diff, key=self.api_key)

        routes = json_response["routes"]
        logger.debug("routes: {!r}".format(routes))
        return routes
