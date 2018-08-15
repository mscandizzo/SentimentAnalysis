import json
from textwrap import dedent as d

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import centroids as ct

app = dash.Dash(__name__)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

vectores , colores, k = ct.create_sample()

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': vectores[:,0],
                    'y': vectores[:,1],
                    #'text': ['a', 'b', 'c', 'd'],
                    #'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                    'name': 'Trace 1',
                    'mode': 'markers',
                    'marker': {'size': 6,'color':colores}
                }
                #,
                #{
                #    'x': [1, 2, 3, 4],
                #    'y': [9, 4, 1, 4],
                #    'text': ['w', 'x', 'y', 'z'],
                #    'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
                #    'name': 'Trace 2',
                #    'mode': 'markers',
                #    'marker': {'size': 12}
                #}
            ]
        }
    ),

    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown(d("""
                **Hover Data**

                Mouse over values in the graph.
            """)),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns')        
    ])
])


@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

if __name__ == '__main__':
    app.run_server(debug=True)
