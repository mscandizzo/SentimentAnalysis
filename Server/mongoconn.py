from pymongo import MongoClient
from urllib.parse import quote_plus
from functools import wraps


def get_mongo_db(db_name, host = 'localhost',\
                 port= 27017,username=None, password=None):
    
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
    
    collection = db[collection]
    resultado = collection.find({})
    lista = list(resultado)

    return lista

def search_field(field=None,collection=None,**kwargs):
    conn = get_mongo_db(**kwargs)[collection]
    return list(conn.find({},{field:1,"_id":0}))


