import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.graph_objs import *
import centroids as ct

app = dash.Dash()

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

#vectores , colores, k = ct.create_sample()


app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions'
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
    centroids = ct.get_random_centroids(vectores,k)
    closest = ct.get_nearest_centroid_for_all_points(vectores,centroids)
    movimiento =ct.looping_centroids(vectores,centroids)
    minix, maxix, miniy,maxiy = ct.bordes(movimiento)

    return {
            'data': [Scatter( x = vectores[:,0],
                           y = vectores[:,1],
                           mode='markers',
                           marker= dict(color=colores)),
                    Scatter( x = vectores[:,0],
                          y = vectores[:,1],
                          mode='markers', 
                          marker= dict(color=colores))
                ],
            'layout': Layout(#width=600, height=600,
                xaxis=dict( range=[minix,maxix],autorange=False, zeroline=False),
                yaxis=dict( range=[miniy,maxiy], autorange=False, zeroline=False),
                title='Kinematic Generation of a Planar Curve', hovermode='closest',
                updatemenus= [{'type': 'buttons',
                            'buttons': [{'label': 'Play',
                                            'method': 'animate',
                                            'args': [None]}]}]
                            ),
            'frames':[dict(data=[dict(x=[movimiento[k][:,0][0],movimiento[k][:,0][1],movimiento[k][:,0][2]], 
                            y=[movimiento[k][:,1][0],movimiento[k][:,1][1],movimiento[k][:,1][2]], 
                            mode='markers', 
                            marker=dict(color='red', size=15)
                            )
                    ]) for k in range(len(movimiento))]

        }

if __name__ == '__main__':
    app.run_server()




    
