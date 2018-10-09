import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import bjjmap, app2


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
    elif pathname == '/apps/app2':
         return app2.layout
    else:
        return bjjmap.layout # return '404'

if __name__ == '__main__':
    app.run_server(debug=True)