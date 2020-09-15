import pandas

from rockclimbing import json_helper
from rockclimbing.geolocation import Geolocation, get_distance
from rockclimbing.logger import logger
from rockclimbing.ratings import yosemite as y_rating, bouldering as b_rating
from rockclimbing.ratings.bouldering import Rating as BRating
from rockclimbing.ratings.yosemite import Rating as YRating


def rating_to_number(rating, climbing_type):
    """
    Takes a rating and type of route and returns a number that represents its magnitude
    :param rating: The rating of the route.  e. g. 5.10a or V5
    :param climbing_type: The type of route.  Options: Trad, Sport, Toprope, or Boulder
    :return: The magnitude of the route bubbles.  Range: 1 to 15
    """
    try:
        if "Trad" in climbing_type or "Sport" in climbing_type or "Toprope" in climbing_type:
            rating_number = y_rating.parse_rating(rating).number
        elif "Boulder" in climbing_type:
            rating_number = (b_rating.parse_rating(rating).number + 1) * YRating.count() / BRating.count()
        else:
            logger.error("Unknown climbing type {}".format(climbing_type))
            raise RuntimeError("Unknown climbing type {}".format(climbing_type))
        return rating_number
    except RuntimeError:
        return None


class RockClimbingDataProvider:
    """
    Creates a DataFrame which contains information on rock climbing routes around a particular latitude and
    longitude.
    """

    url = "https://www.mountainproject.com/data/get-routes-for-lat-lon"

    def __init__(self, latitude, longitude, api_key, max_distance=100, max_results=20, min_diff="5.1", max_diff="5.15"):
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
        self.geolocation = Geolocation(latitude, longitude)
        self.max_distance = max_distance
        self.max_results = max_results
        self.min_diff = min_diff
        self.max_diff = max_diff
        self.api_key = api_key

    def create_routes_data_frame(self):
        """
        Creates a DataFrame containing information on the routes queried.
        """
        logger.debug(
            "self.geolocation: {}, self.max_distance: {}, self.max_results: {}, self.min_diff: {}, self.max_diff: {}".format(
                self.geolocation, self.max_distance, self.max_results, self.min_diff, self.max_diff))

        routes_df = pandas.DataFrame(self._get_routes())

        if routes_df.empty:
            self._assign_lat_lon_df(routes_df)
            return routes_df

        routes_df["distance_from_origin"] = routes_df.apply(
            lambda x: get_distance(
                self.geolocation, Geolocation(x["latitude"], x["longitude"]), unit="mi"),
            axis=1)

        routes_df["rating_number"] = routes_df.apply(
            lambda x: rating_to_number(x["rating"], x["type"]), axis=1)
        routes_df.dropna(subset=["rating_number"], inplace=True)

        index_names = routes_df[routes_df['distance_from_origin'] > self.max_distance].index
        routes_df.drop(index_names, inplace=True)

        if routes_df.empty:
            self._assign_lat_lon_df(routes_df)

        return routes_df

    def _assign_lat_lon_df(self, df):
        df["latitude"] = [self.geolocation.latitude]
        df["longitude"] = [self.geolocation.longitude]
        return df

    def _get_routes(self):
        """Queries https://www.mountainproject.com/data/get-routes-for-lat-lon """
        json_response = json_helper.get_json(
            self.url, lat=self.geolocation.latitude, lon=self.geolocation.longitude,
            maxDistance=self.max_distance, maxResults=self.max_results,
            minDiff=self.min_diff, maxDiff=self.max_diff, key=self.api_key)

        routes = json_response["routes"]
        logger.debug("routes: {!r}".format(routes))
        return routes
