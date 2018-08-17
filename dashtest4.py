import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.graph_objs import *
import centroids as ct
import numpy as np


tito = {'0':(np.array([9.06982824, 5.53485365, 2.44470969]),
        np.array([18.72012163,  3.9961344 , -9.93333596])),
        '1': (np.array([12.04154117,  4.61383521,  3.31072   ]),
            np.array([12.91813703, 13.77653776, -5.84407335]))}



app = dash.Dash()


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div([
    html.H1('KNN Algorithm Implementation'),
    html.Div([
        dcc.Graph(
            id='distributions'
        )]),

    html.Div([
        html.Div([
        dcc.Input(id='clusters', value=3, type='number'),
        html.Div(id='quant-clusters')
                    ],
        style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        html.Div([
        dcc.Input(id='centroids', value='0', type='text'),
        html.Div(id='quant-centroids')
                    ],
        style={'width': '49%', 'float': 'right', 'display': 'inline-block'})

        
        #html.Div([
        #dcc.Slider(
        #    id='cluster-number-slider',
        #    min=1,#int(dictfinal[0][0]),
        #    max=10,#int(dictfinal[-1][0]),
        #    value=10,#int(dictfinal[0][0]),
        #    step=None,
        #    marks= {'1':1,'5':5,'10':10})#mydict)
        #            ],
        #style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
        
        ])
    ])
])
@app.callback(
    Output('distributions','figure'),
    [Input(component_id='clusters', component_property='value')]
    )
def update_output_div(input_value):
    
    vectores , colores, k = ct.create_sample(input_value)
    centroids = ct.get_random_centroids(vectores,k)
    closest = ct.get_nearest_centroid_for_all_points(vectores,centroids)
    movimiento =ct.looping_centroids(vectores,centroids)
    minix, maxix, miniy,maxiy = ct.bordes(movimiento)
    #dictfinal,mydict = ct.vectorizar(movimiento)

    #xvector = mydict[step][0]
    #yvector = mydict[step][1]

    return {
            'data': [Scatter( x = vectores[:,0],
                           y = vectores[:,1],
                           mode='markers',
                           marker= dict(color=colores)),
                    Scatter( x = vectores[:,0],
                          y = vectores[:,1],
                          mode='markers', 
                          marker= dict(color=colores)),
                ],
            'layout': Layout(#width=600, height=600,
                xaxis=dict( range=[minix,maxix],autorange=False, zeroline=False),
                yaxis=dict( range=[miniy,maxiy], autorange=False, zeroline=False),
                hovermode='closest'
                            )
        }


@app.callback(
    Output('distributions','figure'),
    [Input(component_id='centroids', component_property='value')])
def output_centroids(step):
    return {
            'data': [Scatter( x = tito[step][0],
                           y = tito[step][1][1],
                           mode='markers',
                           marker= dict(color=colores))
                ],
            
        }
    


if __name__ == '__main__':
    app.run_server()

