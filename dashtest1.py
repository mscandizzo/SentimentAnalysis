import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import centroids as ct

app = dash.Dash()

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

vectores , colores, k = ct.create_sample()


app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions'#,
        #figure={
        #    'data': [
        #        {
        #            'x': vectores[:,0],
        #            'y': vectores[:,1],
        #            'name': 'Trace 1',
        #            'mode': 'markers',
        #            'marker': {'size': 6,'color':colores}
        #        }
                
        #    ]
        #}
    ),

    html.Div(className='row', children=[
        html.Div([
    dcc.Input(id='my-id', value=3, type='number'),
    html.Div(id='my-div')
                ])    
    ])
])


@app.callback(
    Output('basic-interactions','figure'),
    [Input(component_id='my-id', component_property='value')])
def update_output_div(input_value):
    
    vectores , colores, k = ct.create_sample(input_value)

    return {
            'data': [
                {
                    'x': vectores[:,0],
                    'y': vectores[:,1],
                    'name': 'Trace 1',
                    'mode': 'markers',
                    'marker': {'size': 6,'color':colores}
                }
                
            ]
        }

if __name__ == '__main__':
    app.run_server()




    
