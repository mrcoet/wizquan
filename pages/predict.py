import dash
from dash import Dash, html, dcc, Input, Output, State, callback

import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

from db.orm import get_years, get_months, get_regions

from utils.norm import norm_get_by_region
from utils.prophet import get_prophet


import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path='/predict',
    title='predict a year of temp',
    name='predict a year of temp')


layout = dmc.Container(
    children=[
        dcc.Markdown("""
        # Predict 2021 Temperature
        By month average and per region. using [Prophet](https://github.com/facebook/prophet) model. Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well. 
        """),
        dmc.Group(
            children=[
                dmc.Select(
                    label="Select region",
                    placeholder="Select a region",
                    id="pred_select_region",
                    value="65",
                    data=get_regions(),
                ),
                dmc.Button(
                    "Show",
                    id='pred_button_show',
                    leftIcon=[DashIconify(
                        icon="fluent:database-plug-connected-20-filled")],
                    style={'margin-top': '25px'}
                ),

            ],
            grow=True,
            class_name='mb-5',

        ),
        dcc.Loading(
            [
            dmc.Group(
                [
                    dcc.Graph(id='training'),],
                grow=True,
                class_name='mt-5, mb-5'
            ),
            dmc.Group(
                [
                    dcc.Graph(id='predicting')],
                grow=True,
                class_name='mt-5, mb-5'
            )])
    ],
    class_name='mt-5'

)

@callback(
    Output('training', 'figure'),
    Output('predicting', 'figure'),
    Input('pred_button_show', 'n_clicks'),
    State('pred_select_region', 'value'),

)
def get_prediction(n_clicks, region_):
    

    return get_prophet(int(region_))