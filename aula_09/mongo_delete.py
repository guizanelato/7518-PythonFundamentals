
from pymongo import MongoClient

client = MongoClient()

collection = client.pf

collection.pf.delete_one({
            'data': '2020-09-07'
            }
        )

for registro in collection.pf.find():
    print(registro)

