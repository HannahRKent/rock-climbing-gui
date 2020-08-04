# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State

from climbing_data_provider import RockClimbingDataProvider

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data_provider = RockClimbingDataProvider(40.03, -105.25)

app.layout = html.Div([
    html.H1("Rock climbing stuff!", style={"textAlign": "center"}),
    html.Div(children=[
        html.Label("Latitude"),
        dcc.Input(id="input-latitude", value=data_provider.latitude, type="text"),
        html.Label("Longitude"),
        dcc.Input(id="input-longitude", value=data_provider.longitude, type="text"),
        html.Label("Max Distance"),
        dcc.Input(id="input-max-distance", value=data_provider.max_distance, type="text"),
        html.Label("Max Results"),
        dcc.Input(id="input-max-results", value=data_provider.max_results, type="text"),
        html.Label("Min Diff"),
        dcc.Input(id="input-min-diff", value=data_provider.min_diff, type="text"),
        html.Label("Max Diff"),
        dcc.Input(id="input-max-diff", value=data_provider.max_diff, type="text"),
        html.Button("Update", id="button-update"),
    ]),
    dcc.Graph(id="graph-difficulty-vs-rating")
])


@app.callback(
    Output("graph-difficulty-vs-rating", "figure"),
    [Input("button-update", "n_clicks")],
    [
        State("input-latitude", "value"),
        State("input-longitude", "value"),
        State("input-max-distance", "value"),
        State("input-max-results", "value"),
        State("input-min-diff", "value"),
        State("input-max-diff", "value"),
    ])
def update_graph(n_clicks, latitude, longitude, max_distance, max_results, min_diff, max_diff):
    data_provider.latitude = latitude
    data_provider.longitude = longitude
    data_provider.max_distance = int(max_distance)
    data_provider.max_results = int(max_results)
    data_provider.min_diff = min_diff
    data_provider.max_diff = max_diff

    routes = data_provider.create_routes_data_frame()

    if "id" not in routes:
        fig = px.scatter_mapbox(
            routes,
            lat="latitude",
            lon="longitude",
            mapbox_style="open-street-map"
        )
    else:
        fig = px.scatter_mapbox(
            routes,
            lat="latitude",
            lon="longitude",
            color="stars",
            size="rating_number",
            text="name",
            hover_data={
                "rating": True,
                "rating_number": False
            },
            color_continuous_scale=px.colors.diverging.Portland,
            mapbox_style="open-street-map"
        )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
