import numpy as np
import seaborn as sns; sns.set()
from copy import deepcopy
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
from IPython.display import display, HTML
py.sign_in('mscandizzo', 'QA6ByvcoBJcWk7H0NAUi')

def create_sample(k=3,maximizer=6,datapoints=100):
    vectores = np.array([])
    colores = np.array([])
    for i, j in enumerate(range(k)):
        vector = np.random.multivariate_normal([j * maximizer, j * maximizer], [[1, 0], [0, 100]], 100)
        color = np.ones(100)*(j+1)
        vectores = np.append(vectores,vector)
        colores = np.append(colores, color)
    vectores = np.vstack(vectores).reshape((100*k,2))
    colores = np.hstack(colores)
    return vectores, colores, k

def get_random_centroids(vectores, k):
    return vectores[np.random.permutation(len(vectores))[0:k]]

def dist(a,b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

def get_nearest_centroid_for_all_points(vectores,centroids):
    closest = np.zeros(len(vectores))
    for i in range(len(vectores)):
        distances = dist(vectores[i],centroids)
        cluster = np.argmin(distances)
        closest[i] = cluster
    return closest

def move_centroids(vectores,closest,centroids):
    for k in range(centroids.shape[0]):
        cluster = vectores[closest==k]
        centroids[k] = cluster.mean(axis=0)
    return centroids

def looping_centroids(vectores, centroids,max_iteractions=5000,printing=False):
    last_closest =[]
    movimiento = []
    if printing:
        print(centroids)
    movimiento.append(centroids)
    for i in range(max_iteractions):
        closest = get_nearest_centroid_for_all_points(vectores,centroids)
        centroids = move_centroids(vectores,closest,centroids)
        if printing:
            print(centroids)
        datos = deepcopy(centroids)
        movimiento.append(datos)
        if (np.array_equal(last_closest,closest)):
            break
        last_closest = closest
    
    return movimiento 


def run_process(k):
    vectores, colores, k= create_sample()
    centroids = get_random_centroids(vectores,k)
    closest = get_nearest_centroid_for_all_points(vectores,centroids)
    movimiento =looping_centroids(vectores,centroids)
    visualize(vectores,colores,movimiento)

def bordes(movimiento,gap=2):
    minix = 0
    maxix = 0
    miniy = 0
    maxiy = 0
    for i in range(len(movimiento)):
        if np.min(movimiento[i][:,0]) < minix:
            minix = np.min(movimiento[i][:,0])
        if np.max(movimiento[i][:,0]) > maxix:
            maxix = np.max(movimiento[i][:,0])
        if np.min(movimiento[i][:,1]) < miniy:
            miniy = np.min(movimiento[i][:,1])
        if np.max(movimiento[i][:,1]) > maxiy:
            maxiy = np.max(movimiento[i][:,1])
            
    return minix-2,maxix+2,miniy-2,maxiy+2
    
def visualize(vectores,colores,movimiento):
    init_notebook_mode(connected=True)

    minix, maxix, miniy,maxiy = bordes(movimiento)

    data=[dict( x = vectores[:,0],
                y = vectores[:,1],
                mode='markers',
                marker= dict(color=colores)),
        dict( x = vectores[:,0],
                y = vectores[:,1],
                mode='markers', 
                marker= dict(color=colores))
        ]
        
    layout=dict(width=600, height=600,
                xaxis=dict( range=[minix,maxix],autorange=False, zeroline=False),
                yaxis=dict( range=[miniy,maxiy], autorange=False, zeroline=False),
                title='Kinematic Generation of a Planar Curve', hovermode='closest',
                updatemenus= [{'type': 'buttons',
                            'buttons': [{'label': 'Play',
                                            'method': 'animate',
                                            'args': [None]}]}])

    frames=[dict(data=[dict(x=[movimiento[k][:,0][0],movimiento[k][:,0][1],movimiento[k][:,0][2]], 
                            y=[movimiento[k][:,1][0],movimiento[k][:,1][1],movimiento[k][:,1][2]], 
                            mode='markers', 
                            marker=dict(color='red', size=15)
                            )
                    ]) for k in range(len(movimiento))]    



    figure1=dict(data=data , layout=layout,frames=frames)          
    iplot(figure1)
