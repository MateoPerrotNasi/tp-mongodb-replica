import pymongo
import json
from pymongo import MongoClient, InsertOne


def import_data():

        # On se connecte à mongodb
        client = pymongo.MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")
        
        # On instancie de la db et de la collection utilisés
        db = client["test"]
        collection = db["users"]

        # On ouvre le fichier json contenant les fausses données utilisateurs et on les stocke
        with open(r"data.json") as f:
                data = json.load(f)

        # On insère les données stocker dans mongodb
        collection.insert_many(data)

        # On arrête la connexion avec mongodb
        client.close



