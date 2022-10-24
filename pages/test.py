from sre_constants import IN
import dash
from dash import Dash, html, dcc, Input, Output, State, callback

import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

from db.orm import get_years, get_months, get_regions

from utils.norm import norm_get_by_region

import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path='/test',
    title='Check normality for temp',
    name='check normality for temp')

layout = dmc.Container(
    [
        dmc.Select(
            data= [
                {
                    'label': 'home',
                    'value': '1',
                },
                                {
                    'label': 'analytics',
                    'value': '2',
                }
            ],
            style={"width": 600},
            placeholder="Search",
            nothingFound="No match found",
            searchable=True,
            clearable=True,
            icon=[
                DashIconify(icon="radix-icons:magnifying-glass")
            ],
            id ='a1',
        ),
        html.Div(id="hidden_div_for_redirect_callback1")
    ],
    class_name='mt-5'

)

@callback(
    Output('hidden_div_for_redirect_callback1', 'children'),
    Input('a1', 'value')
)
def dd(value_):
    
    if value_ and (int(value_) == 1):
        return dcc.Location(pathname="/", id='any_thing')
