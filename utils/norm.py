import imp
from db import session
from db.models import Polygons, Temperatures, States, Points
import pandas as pd
import numpy as np
import json
import plotly.express as px
import os


def norm_get_by_region(year_id, month_id, region_id) -> list:
    q = session.query(Temperatures
        ).join(
            Points
            ).join(Polygons
            ).filter(Polygons.state_id==region_id
            ).filter(Temperatures.year_id==year_id
            ).filter(Temperatures.month_id==month_id)
    temp = []

    for row in q:
        temp.append(row.temp)
    
    return temp