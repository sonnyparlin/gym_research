import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

# mapbox_access_token = 'ADD_YOUR_TOKEN_HERE'

df = pd.read_csv('https://raw.githubusercontent.com/sonnyparlin/gym_research/master/rkbjj_florida.csv')
site_lat = df.lat
site_lon = df.lon
locations_name = df.text

data = [
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=dict(
            size=17,
            color='rgb(0, 128, 0)',
            opacity=0.7
        ),
        text=locations_name,
        hoverinfo='text'
    )]

layout = go.Layout(
    title='RKBJJ Gyms in Florida',
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        bearing=0,
        center=dict(
            lat=28.025881,
            lon=-81.732880
        ),
        pitch=0,
        zoom=8.3,
        style='light'
    ),
)

fig = dict(data=data, layout=layout)
py.plot(fig, filename='RKBJJ Schools')
