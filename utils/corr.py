import imp

from matplotlib.pyplot import colorbar
from db import session
from db.models import Monthly_avg, Polygons, Temperatures, States, Points
import pandas as pd
import numpy as np
import json
import plotly.express as px
import os
import plotly.graph_objects as go
import plotly.figure_factory as ff

# def get_corr(year_id, month_id, regions_list):
#     dataset = {}
#     for region_id in regions_list:
#         tem_list = []
#         reg_ = session.query(States).filter(States.id==region_id).first()
#         reg_name = reg_.name
#         q = session.query(Temperatures
#             ).join(Points
#             ).join(Polygons
#             ).filter(Polygons.state_id==region_id
#             ).filter(Temperatures.year_id==year_id
#             ).filter(Temperatures.month_id==month_id
#             ).all()

#         for row in q:
#             tem_list.append(row.temp)

#         dataset[reg_name] = tem_list

#     df = pd.DataFrame(dataset)

#     df_corr = df.corr() # Generate correlation matrix

#     fig = go.Figure()
#     fig.add_trace(
#         go.Heatmap(
#             x = df_corr.columns,
#             y = df_corr.index,
#             z = np.array(df_corr)
#         )
#     )

#     return fig


# def get_corr(regions_list):
#     dataset = {}
#     for region_id in regions_list:
#         tem_list = []
#         reg_ = session.query(States).filter(States.id==region_id).first()
#         reg_name = reg_.name
#         q = session.query(Monthly_avg).filter(Monthly_avg.state_id==region_id).all()

#         for row in q:
#             tem_list.append(row.temp)

#         dataset[reg_name] = tem_list

#     df = pd.DataFrame(dataset)
#     print(df)
#     df_corr = df.corr() # Generate correlation matrix

#     fig = go.Figure()
#     fig.add_trace(
#         go.Heatmap(
#             x = df_corr.columns,
#             y = df_corr.index,
#             z = np.array(df_corr)
#         )
#     )

#     return fig


def get_corr(regions_list):
    dataset = {}
    for region_id in regions_list:
        tem_list = []
        reg_ = session.query(States).filter(States.id == region_id).first()
        reg_name = reg_.name
        q = session.query(Monthly_avg).filter(
            Monthly_avg.state_id == region_id).all()

        for row in q:
            tem_list.append(row.temp)

        dataset[reg_name] = tem_list

    df = pd.DataFrame(dataset)

    df_corr = df.corr()  # Generate correlation matrix

    fig = go.Figure(
        data=go.Heatmap(
            z=df_corr,
            x=df_corr.index.values,
            y=df_corr.columns.values,
            colorscale='Blues',
            zmin=0.9,
    )
    )

    fig.update_layout(
        title='Correlation Heatmap',
        barmode='overlay',
        plot_bgcolor='#2C2F33',
        paper_bgcolor='#2C2F33',
        font={
            "size": 12,
            "color": '#C1C2C5',
            "family": 'Segoe UI, Roboto'
        },
        xaxis={
            'showgrid': False,
            'zeroline': False
        },
        yaxis={
            'showgrid': False,
            'zeroline': False
        },
    )

    return fig
