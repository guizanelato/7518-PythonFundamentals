
from pymongo import MongoClient

client = MongoClient()

collection = client.pf

for registro in collection.pf.find():
    print(registro)
