# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import os
import sys
sys.path.append(os.getcwd())
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State

import rockclimbing.ratings.bouldering as b_rating
import rockclimbing.ratings.yosemite as y_rating
from rockclimbing.climbing_data_provider import RockClimbingDataProvider

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

data_provider = RockClimbingDataProvider(40.03, -105.25, os.getenv("APIKEY"))

state_routes_df = pd.read_csv(os.path.join("data", "number_of_routes_by_state.csv"))
df_state_abbrevations = pd.read_csv(os.path.join("data", "lat_lon_states.csv"))
state_routes_df = pd.merge(state_routes_df, df_state_abbrevations)


def construct_yosemite_ratings_dict():
    r_dict = {}
    for rating in y_rating.Rating:
        if rating.number.is_integer():
            r_dict[int(rating.number)] = str(rating).replace("a", "")
        else:
            r_dict[rating.number] = ""
    return r_dict


yosemite_ratings_dict = construct_yosemite_ratings_dict()
bouldering_ratings_dict = {rating.number: str(rating) for rating in b_rating.Rating}


def make_choropleth_fig(df):
    fig = px.choropleth(
        df,
        locations="state",
        color="number_of_routes",
        locationmode="USA-states",
        scope="usa",
        color_continuous_scale="Reds",
        title='Rock climbing routes per state',
        custom_data=["latitude", "longitude"]
    )
    return fig


# Starting data for the scatterplot.
app.layout = html.Div([
    html.H1("Rock climbing stuff!", style={"textAlign": "center"}),
    html.Div([
        dcc.Graph(id='choropleth-states', figure=make_choropleth_fig(state_routes_df)),
        html.Div(id='selected-state'),
        html.Div(id='selected-coordinates'),
        html.Hr()
    ]),
    html.Div([
        dcc.RadioItems(
            id='route-type',
            options=[
                {'label': 'Bouldering Routes', 'value': 'boulder'},
                {'label': 'Rock Climbing Routes', 'value': 'rock'}
            ],
            value='rock'
        ),
        html.Hr(),
        dcc.RangeSlider(id='rating-range'),
        html.Hr(),
    ]),
    html.Div(children=[
        html.Label("Max Distance"),
        dcc.Input(id="input-max-distance", value=data_provider.max_distance, type="text"),
        html.Label("Max Results"),
        dcc.Input(id="input-max-results", value=data_provider.max_results, type="text"),
        html.Button("Update", id="button-update"),
    ]),
    dcc.Graph(id="graph-difficulty-vs-rating")
])


@app.callback(
    Output('selected-state', 'children'),
    [Input('choropleth-states', 'clickData')]
)
def show_selected_state(click_data):
    selected_state = "None"
    if click_data is not None:
        selected_state = click_data["points"][0]["location"]
    return 'Selected State: {}'.format(selected_state)


@app.callback(
    Output('selected-coordinates', 'children'),
    [Input('choropleth-states', 'clickData')]
)
def show_selected_state(click_data):
    selected_coordinates = "None"
    if click_data is not None:
        selected_coordinates = list(click_data["points"][0]["customdata"])
    return 'Selected Coordinates: {}'.format(selected_coordinates)


@app.callback(
    [Output('rating-range', 'min'),
     Output('rating-range', 'max'),
     Output('rating-range', 'step'),
     Output('rating-range', 'marks'),
     Output('rating-range', 'value')],  # may have to put the value in a callback further down
    [Input('route-type', 'value')]
)
def set_slider_options(climbing_type):
    if climbing_type == "boulder":
        min_value = b_rating.Rating.V0.number,
        max_value = b_rating.Rating.V17.number,
        step = None,
        marks = bouldering_ratings_dict,
        value = [b_rating.Rating.V0.number, b_rating.Rating.V17.number]
    elif climbing_type == "rock":
        min_value = y_rating.Rating.Y51.number,
        max_value = y_rating.Rating.Y515D.number,
        step = None,
        marks = yosemite_ratings_dict,
        value = [y_rating.Rating.Y51.number, y_rating.Rating.Y515D.number]
    else:
        raise RuntimeError("Unknown climbing type {}".format(climbing_type))
    return min_value[0], max_value[0], step[0], marks[0], value


@app.callback(
    Output("graph-difficulty-vs-rating", "figure"),
    [Input("button-update", "n_clicks"),
     Input("route-type", "value"),
     Input("rating-range", "value"),
     Input('choropleth-states', 'clickData')],
    [State("input-max-distance", "value"),
     State("input-max-results", "value")]
)
def update_graph(n_clicks, route_type, rating_range, click_data, max_distance, max_results):
    """

    :param n_clicks:
    :param route_type:
    :param rating_range:
    :param click_data:
    :param max_distance:
    :param max_results:
    :return:
    """

    if click_data is not None:
        data_provider.geolocation.latitude, data_provider.geolocation.longitude = click_data["points"][0]["customdata"]
    data_provider.max_distance = int(max_distance)
    data_provider.max_results = int(max_results)

    if route_type == "rock":
        data_provider.min_diff = y_rating.from_number(rating_range[0]).value
        data_provider.max_diff = y_rating.from_number(rating_range[1]).value
    else:
        data_provider.min_diff = b_rating.from_number(rating_range[0]).value
        data_provider.max_diff = b_rating.from_number(rating_range[1]).value

    routes = data_provider.create_routes_data_frame()

    if "id" not in routes or routes.id.isnull().all():
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
            color="rating_number",
            size="stars",
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
