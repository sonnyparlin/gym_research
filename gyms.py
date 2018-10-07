import plotly.plotly as py
import plotly.graph_objs as go
import distance
import pandas as pd

# mapbox_access_token = 'ADD_YOUR_TOKEN_HERE'

df = pd.read_csv('https://raw.githubusercontent.com/sonnyparlin/gym_research/master/rkbjj_florida.csv')
site_lat = df.lat
site_lon = df.lon
locations_name = df.text
dist = distance.build_distance_tuples()
s=""
for a, b, c in dist:
    s += "<span name=\"dist\">{} is {} miles from {}</span><br/>".format(a,c,b)
    
file = open('distance.html', 'w')
file.write("""
<html>
    <head>
        <title>Gracie Tampa Gyms</title>
    </head>
    <body style='font: 11px arial, sans-serif;'>
            <table>
                <tr>
                    <td>
                    <img src="https://raw.githubusercontent.com/sonnyparlin/gym_research/master/RKBJJSchools.png" />
                    </td>
                
                    <td style='padding-left:20px;font: 12px arial, sans-serif;'>
                    <div>{}</div>
                    </td>
                </tr>
            </table>
    
    </body>
    </html>""".format(s))
file.close()

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
