import dash
from dash import Dash, html, dcc, Input, Output, State, callback

import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

from utils.map import draw_tem_russia, empty_russia
from db.orm import get_years, get_months

dash.register_page(__name__, path='/')

layout = dmc.Container(
    children=[
        dcc.Markdown(
            """
                    # Russia Historical Temp. Data
                    By region monthly average.
                    """,
            className='mb-5',
            mathjax=True,
        ),
        dmc.Group(
            children=[
                dmc.Select(
                    label='Select year',
                    placeholder='Select a year',
                    id='select_years',
                    value="2022",
                    data=get_years(),
                ),
                dmc.Select(
                    label="Select month",
                    placeholder="Select a month",
                    id="select_months",
                    value="1",
                    data=get_months(),
                ),
                dmc.Button(
                    "Show",
                    id='button_show',
                    leftIcon=[DashIconify(
                        icon="fluent:database-plug-connected-20-filled")],
                    style={'margin-top': '26px'}
                ),

            ],
            direction='row',
            grow=True,
            position='center',
            spacing='xl',

        ),
        dcc.Loading(
            dcc.Graph(
                figure=empty_russia(),
                className='mt-5',
                id='map_fig',
                config={"displayModeBar": False}),
        ),
    ],
    class_name='mt-5',

)


@callback(
    Output(component_id='map_fig', component_property='figure'),
    Input('button_show', 'n_clicks'),
    State('select_years', 'value'),
    State('select_months', 'value'), prevent_initial_call=True
)
def update_map(n_clicks, year_, month_):
    print(year_)
    print(month_)
    return draw_tem_russia(int(year_), int(month_))
