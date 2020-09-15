"""Test data for climbing_data_provider tests"""
import pandas

url = "https://www.mountainproject.com/data/get-routes-for-lat-lon?lat=40.03&lon=-105.25&maxDistance=100&maxResults=20"\
      "&minDiff=5.1&maxDiff=5.15&key=test_key"

json_response = """
{
    "routes": [],
    "success": 1
}
"""

expected_df = pandas.DataFrame({
    'latitude': [40.03],
    'longitude': [-105.25]
})
