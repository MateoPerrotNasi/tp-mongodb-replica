import pymongo
import json
from pymongo import MongoClient, InsertOne


def import_data():
        client = pymongo.MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")

        db = client["test"]
        collection = db["users"]


        with open(r"data.json") as f:
                data = json.load(f)


        collection.insert_many(data)
        client.close



