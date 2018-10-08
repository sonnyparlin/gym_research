import plotly.plotly as py
import plotly.graph_objs as go
import distance
import pandas as pd

# mapbox_access_token = 'ADD_YOUR_TOKEN_HERE'

df = pd.read_csv('https://raw.githubusercontent.com/sonnyparlin/gym_research/master/rkbjj_florida.csv')
site_lat = df.lat
site_lon = df.lon
locations_name = df.text
    
trace = go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers+text',
        textposition='middle right',
        marker=dict(
            size=17,
            color='rgb(0, 128, 0)',
            opacity=0.7
        ),
        text=locations_name,
        hoverinfo='text'
    )

layout = go.Layout(
    title='RKBJJ Gyms in Florida',
    autosize=False,
    width=1000,
    height=600,
    showlegend=False,
    hovermode='closest',
    mapbox=dict(
        bearing=0,
        center=dict(
            lat=27.849172,
            lon=-82.234936
        ),
        pitch=20,
        zoom=8.5,
        style='light'
    ),
)

data = [trace]
fig = dict(data=data, layout=layout)
py.plot(fig, filename='RKBJJ Schools')
