import sys
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup


def _coordinate_to_float(entry):
    return float(entry.replace("–", "-"))


def _scrape_county_data():
    response = requests.get("https://en.wikipedia.org/wiki/User:Michael_J/County_table")
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select(".wikitable>tbody>tr")
    county_locations_data = {"fips": [], "state_code": [], "name": [], "latitude": [], "longitude": []}
    for row in rows[1:]:
        entries = row.find_all("td")
        county_locations_data["fips"].append(entries[2].text)
        county_locations_data["state_code"].append(entries[1].text)
        county_locations_data["name"].append(entries[3].text)
        county_locations_data["latitude"].append(_coordinate_to_float(entries[12].text[:-1]))
        county_locations_data["longitude"].append(_coordinate_to_float(entries[13].text[:-2]))

    return pd.DataFrame(data=county_locations_data)


def create_county_data_csv(file):
    file.parent.mkdir(exist_ok=True)
    df = _scrape_county_data()
    df.to_csv(sys.argv[1], index=False)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        create_county_data_csv(Path(sys.argv[1]))
    else:
        print("Usage: python county_location_gatherer.py target.csv")
