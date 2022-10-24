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
    path='/normality',
    title='Check normality for temp',
    name='check normality for temp')

layout = dmc.Container(
    children=[
        dcc.Markdown("""
        # Check normality for Temp.
        By month per year.
        """),
        dmc.Group(
            children=[
                dmc.Select(
                    label='Select year',
                    placeholder='Select a year',
                    id='norm_select_years',
                    value="2022",
                    data=get_years(),
                ),
                dmc.Select(
                    label="Select month",
                    placeholder="Select a month",
                    id="norm_select_months",
                    value="1",
                    data=get_months(),
                ),
                dmc.Select(
                    label="Select region",
                    placeholder="Select a region",
                    id="norm_select_region",
                    value="65",
                    data=get_regions(),
                ),
               dmc.Button(
                    "Show",
                    id='norm_button_show',
                    leftIcon=[DashIconify(
                        icon="fluent:database-plug-connected-20-filled")],
                    style={'margin-top': '25px'}
                ),
               
            ],
            grow=True,

        ),
        dcc.Loading(
            dmc.Group(
                [
                    dcc.Graph(id='histogram'),
                    dcc.Graph(id='boxplot')],
                grow=True,
                class_name='mt-5'
            ))

    ],
    class_name='mt-5'

)


@callback(
    Output('histogram', 'figure'),
    Output('boxplot', 'figure'),
    Input('norm_button_show', 'n_clicks'),
    State('norm_select_years', 'value'),
    State('norm_select_months', 'value'),
    State('norm_select_region', 'value'),

)
def check_norm(n_clicks, years_, months_, region_):
    data: list = norm_get_by_region(int(years_), int(months_), int(region_))

    df = pd.DataFrame({'temp': data})

    bfig = px.box(df, y="temp")
    bfig.update_layout(title='Tem. Heatmap Russia')
    bfig.update_layout(
        title='Tem. Boxplot',
        barmode='overlay',
        plot_bgcolor='#2C2F33',
        paper_bgcolor='#2C2F33',
        font={
            "size": 12,
            "color": '#C1C2C5',
            "family": 'Segoe UI, Roboto'
        },
        xaxis={
            'title': 'Temperature avg.',
            'showgrid': False,
            'zeroline': False
        },
        yaxis={
            'title': '',
            'showgrid': False,
            'zeroline': False
        },

    )

    hfig = px.histogram(df, x="temp", labels={
                        'x': 'Temperature avg.', 'y': 'count'})

    hfig.update_layout(
        title='Tem. Histogram',
        barmode='overlay',
        plot_bgcolor='#2C2F33',
        paper_bgcolor='#2C2F33',
        font={
            "size": 12,
            "color": '#C1C2C5',
            "family": 'Segoe UI, Roboto'
        },
        xaxis={
            'title': 'Temperature avg.',
            'showgrid': False,
            'zeroline': False
        },
        yaxis={
            'title': 'count',
            'showgrid': False,
            'zeroline': False
        },
    )

    return hfig, bfig
