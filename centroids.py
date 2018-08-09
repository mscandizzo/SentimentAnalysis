import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
from copy import deepcopy

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

def looping_centroids(vectores, centroids,max_iteractions=5000):
    last_closest =[]
    movimiento = []
    print(centroids)
    movimiento.append(centroids)
    for i in range(max_iteractions):
        closest = get_nearest_centroid_for_all_points(vectores,centroids)
        centroids = move_centroids(vectores,closest,centroids)
        print(centroids)
        movimiento.append(deepcopy(centroids))
        if (np.array_equal(last_closest,closest)):
            break
        last_closest = closest
    
    return movimiento 


def run_process():
    vectores, colores, k= create_sample()
    centroids = get_random_centroids(vectores,k)
    closest = get_nearest_centroid_for_all_points(vectores,centroids)
    movimiento =looping_centroids(vectores,centroids,closest)
    return movimiento

