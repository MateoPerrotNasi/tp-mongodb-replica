import pymongo

def update_age():

        client = pymongo.MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")

        db = client["test"]
        collection = db["users"]


        resultat = collection.update_many({},{"$inc": {"age": 5}})

        client.close
