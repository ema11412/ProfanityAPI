from pymongo import MongoClient


MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['docStore']

collection = db['docs']

