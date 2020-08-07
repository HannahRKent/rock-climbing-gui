import requests

from logger import logger


def _build_url(url, **params):
    """Builds a url for an API query out of a dictionary of parameters"""
    if params:
        query_params = map(lambda param: "{}={}".format(*param), params.items())
        return "{}?{}".format(url, "&".join(query_params))
    else:
        return url


def get_json(base_url, **params):
    """
    Builds and queries an API URL
    :param base_url: The URL to which the parameters are appended
    :param params: A dictionary of parameters to query
    :return: Data pulled from the API Query
    """
    url = _build_url(base_url, **params)
    logger.info("API url: {}".format(url))
    return requests.get(url).json()
