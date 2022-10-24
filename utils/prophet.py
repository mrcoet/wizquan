import imp
from sre_parse import State
from db import session
from db.models import Polygons, Temperatures, States, Points, Monthly_avg
import pandas as pd
import numpy as np
import json
import plotly.express as px
import os
from neuralprophet import NeuralProphet
import plotly.graph_objects as go
from sklearn.metrics import mean_absolute_error

def get_prophet(state_id):
    dataset = {'date': [], 't2m': []}
    q = session.query(Monthly_avg
        ).filter(Monthly_avg.state_id == state_id
    ).all()

    for row in q:
        dataset['date'].append(f'{row.year_id}-{row.month_id}-01')
        if row.temp:
            dataset['t2m'].append(int(row.temp))
        else:
            dataset['t2m'].append(np.nan)
    
    df = pd.DataFrame(dataset)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].apply(lambda x: x.year)
    df_train = df[df['year'] <= 2020]
    df_test = df[df['year'] == 2021]
    df_train = df_train[['date', 't2m']]

    df_train.columns = ['ds', 'y']

    
    m = NeuralProphet()
    model = m.fit(df_train, freq='m')

    future = m.make_future_dataframe(df_train, periods=12)
    forecast = m.predict(future)
    # forecast['ds'] = forecast['ds'].values.astype('datetime64[M]')
    forecast['ds'] = forecast['ds'] + pd.offsets.MonthBegin(1)
    # print(forecast)

    fig_train = px.line(df_train, x='ds', y='y', title='Training Set')
    # fig_test = px.line(df_test, x='date', y='t2m', title='Testing Set')
    fig_test = go.Figure()
    fig_test.add_trace(go.Scatter(x=df_test.date, y=df_test.t2m, mode='lines+markers', name='actual'))
    fig_test.add_trace(go.Scatter(x=forecast.ds, y=forecast.yhat1, mode='lines+markers', name='predicted'))
    df_test.reset_index(inplace=True)
    result = pd.concat([forecast[['ds', 'yhat1']], df_test], axis=1)
    result.dropna(axis=0, how='any', inplace=True)

    mae = mean_absolute_error(result['yhat1'], result['t2m'])

    fig_train.update_layout(
        title='Plot chart for Training Set',
        barmode='overlay',
        plot_bgcolor='#2C2F33',
        paper_bgcolor='#2C2F33',
        font={
            "size": 12,
            "color": '#C1C2C5',
            "family": 'Segoe UI, Roboto'
        },
        xaxis={
            'title': 'date',
            'showgrid': False,
            'zeroline': False
        },
        yaxis={
            'title': 'avg. temperature',
            'showgrid': False,
            'zeroline': False
        },
    )

    fig_test.update_layout(
        title=f'Predicted chart with MAE: {round(mae,2)}',
        barmode='overlay',
        plot_bgcolor='#2C2F33',
        paper_bgcolor='#2C2F33',
        font={
            "size": 12,
            "color": '#C1C2C5',
            "family": 'Segoe UI, Roboto'
        },
        xaxis={
            'title': 'months',
            'showgrid': False,
            'zeroline': False
        },
        yaxis={
            'title': 'avg. temperature',
            'showgrid': False,
            'zeroline': False
        },
    )
    
    return fig_train, fig_test
    

        


