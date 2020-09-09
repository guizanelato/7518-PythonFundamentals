
from pymongo import MongoClient

#1: iniciarlizar a conexão
client = MongoClient()

#2: acessar/criar uma collection
collection = client.pf


#3: inserir na collection pf

collection.pf.insert_one(
            {
                'ação': 'estava ao vivo ministrando o Python Fundamentals',
                'data': '2020-09-02'
            }
        )

