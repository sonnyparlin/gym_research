import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps import bjjmap

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, 
    meta_tags=[
    {
        'name': 'description',
        'content': 'App that shows the network gyms'
    }])
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([ 
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content') 
])

app.title="BJJ Map"

@app.callback(
    Output('page-content', 'children'), 
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/bjjmap':
         return bjjmap.layout
    else:
        return bjjmap.layout # return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
