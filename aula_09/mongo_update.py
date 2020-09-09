
from pymongo import MongoClient

try:
    client = MongoClient()
except Exception as err: 
    print('Erro ao conectar com o mongod -', err)

else:
    collection = client.pf


    # antes 

    for registro in collection.pf.find():
        print(registro)


    collection.pf.update_one({'obs': 'Ótima pergunta do Oscar sobre credenciais'},
                {'$set' : 
                    { 
                        'data':'2020-09-07' 
                }})

    print('--------------------------')

    
    for registro in collection.pf.find():
        print(registro)
