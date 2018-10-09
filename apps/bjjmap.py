import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import pandas as pd
import plotly.plotly as py
import geopy.distance

from app import app

df = pd.read_csv('https://raw.githubusercontent.com/sonnyparlin/gym_research/master/rkbjj_florida.csv')

layout = html.Div([
    html.H1('RKBJJ Gyms'),
    html.Div(id='text-content'),
    dcc.Graph(id='map', figure={
        'data': [
            {
                'lat': df['lat'],
                'lon': df['lon'],
                'mode':'markers+text',
                'textposition':'middle right',
                'text': df['gyms'],
                'type': 'scattermapbox',
                'marker': {
                    'color': 'rgb(0, 128, 0)',
                    'size': 12,
                    'opacity': 0.6
                },
                'selected': {
                    "marker": {
                        "color": "red",
                        'size':16
                    }
                },
                'unselected': {
                    "marker": {
                        'color': 'rgb(0, 128, 0)',
                        'size': 12,
                    }
                },
            }
        ],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1Ijoic29ubnlqaXRzdSIsImEiOiJjam14bTFta3QwYXhyM3FtOWZqazZpNGJxIn0.omNsN52xtBl4_zHjSEHDVw',
                'bearing':0,
                'center'  : {
                        'lat':'27.849172',
                        'lon':'-82.234936'
                    },
                'pitch':20,
                'zoom':8.5,
                'style':'light'
            },
            'clickmode': 'select+event',
            'hovermode': 'closest',
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
        }
    })
], style={'marginLeft': 50, 'marginRight': 50, 'marginTop':20})


def distance(lat1, lon1, lat2, lon2):
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    return geopy.distance.vincenty(coords_1, coords_2).miles

@app.callback(
    Output('text-content', 'children'),
    [Input('map', 'selectedData')])
def update_text(selectedData):
    s=""
    di = ""
    try:
        lat1 = selectedData['points'][0]['lat']
        lon1 = selectedData['points'][0]['lon']
        lat2 = selectedData['points'][1]['lat']
        lon2 = selectedData['points'][1]['lon']
        di = distance(lat1, lon1, lat2, lon2)
    except (TypeError, IndexError) as e:
        pass
    
    try:
        return html.H3(
            '{} is {:.1f} miles away from {}'.format(selectedData['points'][0]['text'], di, selectedData['points'][1]['text'])
        )
    except (TypeError, IndexError) as e:
        return html.H3("Hold the shift key and click on two different points to see their distance.")

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})