# Required libraries

from pymongo import MongoClient
from urllib.parse import quote_plus
from functools import wraps


def get_mongo_db(db_name, host = 'localhost',\
                 port= 27017,username=None, password=None):
    '''
    By default it will connect to the localhost and default port
    Optional: To provide username and password
    '''
    
    if username and password:
        uri = "mongodb://%s:%s@%s/%s" % (quote_plus(username), 
                                    quote_plus(password), 
                                    host,
                                    db_name)
        conn = MongoClient(uri)
    else: 
        conn = MongoClient(host, port)
    return conn[db_name]

def db_to_list(db, collection):
    '''
    Simple search to retrieve all data for a given database.

    MongoDB find feature is an iterable so in order to store all data 
    a list is generated and retrieved.
    '''
    
    collection = db[collection]
    resultado = collection.find({})
    lista = list(resultado)

    return lista

def search_field(field=None,collection=None,**kwargs):
    '''
    Simple search to retrieve all data from only one field for each record 
    in the collection
    '''

    conn = get_mongo_db(**kwargs)[collection]

    lista = list(conn.find({}, {field: 1, "_id": 0}))
    
    return lista


