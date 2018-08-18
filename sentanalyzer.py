import mongoconn as con
from textblob import TextBlob
from numpy import asarray

def sentiment(collection='tweets',db_name='tweets'):

    lista =[]
    tweets = con.search_field(field ='text',collection=collection,db_name=db_name)
    for tweet in tweets:
        try:
            polaridad = TextBlob(tweet['text']).polarity
            
            if polaridad >= 0.75:
                lista.append((polaridad,5))
            elif polaridad >.25 and polaridad <.75:
                lista.append((polaridad,4))
            elif polaridad > -.25 and polaridad <= 0.25:
                lista.append((polaridad,3))
            elif polaridad > -.75 and polaridad < 0.25:
                lista.append((polaridad,2))
            else:
                lista.append((polaridad,1))
        except:
            pass
    
    sentimiento = asarray(lista)

    return sentimiento
