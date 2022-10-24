import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify
from dash import Dash, html, dcc, Input, Output, State, callback

def create_home_link(label):
    return dmc.Text(
        label,
        size="xl",
        color="gray",
    )

header = dmc.Header(
    height=70,
    # fixed=True, # uncomment this line if you are using this example in your app
    p="md",
    children=[
        html.Div(id="hidden_div_for_redirect_callback"),
        dmc.Container(
            fluid=True,
            children=dmc.Group(
                position="apart",
                align="flex-start",
                children=[
                    dmc.Center(
                        dcc.Link(
                            [
                                dmc.MediaQuery(
                                    create_home_link("Weather Analysis App"),
                                    smallerThan="sm",
                                    styles={"display": "none"},
                                ),
                                dmc.MediaQuery(
                                    create_home_link("WIZQuan"),
                                    largerThan="sm",
                                    styles={"display": "none"},
                                ),
                            ],
                            href="/",
                            style={"paddingTop": 5, "textDecoration": "none"},
                        ),
                    ),
                    dmc.Group(
                        position="right",
                        align="center",
                        spacing="xl",
                        children=[
                            dmc.MediaQuery(
                                dmc.Select(
                                    data=[
                                        {'label': 'home', 'value':'home'},
                                        {'label': 'normality', 'value': 'normality'},
                                        {'label': 'correlation', 'value': 'correlation'},
                                        {'label': 'predict', 'value': 'predict'}
                                    ],
                                    # style={"width": 250},
                                    placeholder="Search",
                                    nothingFound="No match found",
                                    searchable=True,
                                    clearable=True,
                                    icon=[
                                        DashIconify(icon="radix-icons:magnifying-glass")
                                    ],
                                    id='main_menu'
                                ),
                                smallerThan="md",
                                styles={"width": 120},
                            ),
                            html.A(
                                dmc.Tooltip(
                                    dmc.ThemeIcon(
                                        DashIconify(
                                            icon="radix-icons:github-logo",
                                            width=22,
                                        ),
                                        radius=30,
                                        size=36,
                                        variant="outline",
                                        color="gray",
                                    ),
                                    label="Source Code",
                                    position="bottom",
                                ),
                                href="https://github.com/snehilvj/dash-mantine-components",
                            ),
                            
                        ],
                    ),
                ],
            ),
        )
    ],
)


@callback(
    Output('hidden_div_for_redirect_callback', 'children'),
    Input('main_menu', 'value')
)
def dd(value_):
    
    if value_ and (value_ == 'home'):
        return dcc.Location(pathname="/", id='any-id')
    elif value_ and (value_ == 'normality'):
        return dcc.Location(pathname="/normality", id='any-id')
    elif value_ and (value_ == 'correlation'):
        return dcc.Location(pathname="/correlation", id='any-id')
    elif value_ and (value_ == 'predict'):
        return dcc.Location(pathname="/predict", id='any-id')
