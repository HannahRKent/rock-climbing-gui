import requests

from logger import logger


def _build_url(url, **params):
    if params:
        query_params = map(lambda param: "{}={}".format(*param), params.items())
        return "{}?{}".format(url, "&".join(query_params))
    else:
        return url


def get_json(base_url, **params):
    url = _build_url(base_url, **params)
    logger.info("API url: {}".format(url))
    return requests.get(url).json()
