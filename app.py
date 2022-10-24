from distutils.log import debug
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import Dash, html, page_container

from dmc.header import header

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ],
    external_scripts=[
        "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"
    ],
    use_pages=True,
)


component = dmc.MantineProvider(
    withGlobalStyles=True, theme={"colorScheme": "dark"})

component.children = [
    header,
    html.Div(
        page_container
    )
]

app.layout = component



if __name__ == '__main__':
    app.run_server(debug=True)