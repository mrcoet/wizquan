import dash
from dash import Dash, html, dcc, Input, Output, State, callback

import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

from db.orm import get_years, get_months, get_regions

from utils.norm import norm_get_by_region
from utils.corr import get_corr


import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path='/correlation',
    title='Check correlation for temp',
    name='check correlation for temp')

layout = dmc.Container(
    [
        dcc.Markdown("""
        # Check Correlation between regions.
        Depend on monthly average mean of Temperature.
        """),
        dmc.Group(
            [
                dmc.MultiSelect(
                    data=get_regions(),
                    searchable=True,
                    nothingFound="No cities found",
                    id='corr_options',
                    value=['1', '70', '10', '19'],
                    label="Select regions:",
                ),

            ],
            grow=True
        ),
        dmc.Group(
            [
                dmc.Button(
                "Show",
                id='corr_button_show',
                leftIcon=[DashIconify(
                    icon="fluent:database-plug-connected-20-filled")],
            ),
            ],
            position='right',
            class_name='mt-3 mb-3'
        ),

        dcc.Loading(dcc.Graph('corr_graph'))
    ],
    class_name='mt-5'

)


@callback(
    Output('corr_graph', 'figure'),
    State('corr_options', 'value'),
    Input('corr_button_show', 'n_clicks')

)
def update_corr(regions, n_clicks):
    regions = [int(x) for x in regions]
    return get_corr(regions)