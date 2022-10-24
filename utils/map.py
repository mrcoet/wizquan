import imp
from db import session
from db.models import Polygons, Temperatures, States, Points
import pandas as pd
import numpy as np
import json
import plotly.express as px
import os


absolute_path = os.path.dirname(__file__)


with open(os.path.join(absolute_path, 'geo.json')) as res:
    regions = json.load(res)


def draw_tem_russia(year: int = 2022, month: int = 1):
    values = []
    for s in session.query(States).all():
        q = session.query(Temperatures
            ).join(Points
            ).join(Polygons
            ).filter(Polygons.state_id==s.id
            ).filter(Temperatures.year_id==year
            ).filter(Temperatures.month_id==month).all()
        
        temp_ = []
        for row in q[:10]:
            temp_.append(row.temp)
        values.append(round(np.array(temp_).mean(),0))
    
    cartodb = []
    for i in regions['features']:
        cartodb.append(i['properties']['NAME_1'])
    
    df = pd.DataFrame({"Location": cartodb, "Temperature": values})

    fig = px.choropleth_mapbox(
    df, 
    geojson=regions, 
    color="Temperature",
    locations="Location",
    featureidkey="properties.NAME_1",
    center={"lat": 70, "lon": 100},
    mapbox_style="carto-positron", 
    zoom=1.6,
    opacity=0.5)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"l":0, "t": 0,"b":0})
    fig.update_layout(title='Tem. Heatmap Russia')
    fig.update_layout(plot_bgcolor='#2C2F33', 
                        paper_bgcolor='#2C2F33',
                        font= {
                            "size": 12,
                            "color": '#C1C2C5'})

    return fig


def empty_russia():
    df = pd.DataFrame()
    fig = px.choropleth_mapbox( 
    df,
    center={"lat": 70, "lon": 100},
    mapbox_style="carto-positron", 
    opacity=0.5)

    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=2)
    fig.update_layout(margin={"r":0,"l":0, "t": 0,"b":0})
    fig.update_layout(title='Tem. Heatmap Russia')
    fig.update_layout(plot_bgcolor='#2C2F33', 
                        paper_bgcolor='#2C2F33',
                        font= {
                            "size": 12,
                            "color": '#C1C2C5'})

    return fig
