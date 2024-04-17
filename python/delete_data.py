import pymongo

def delete_data(delete_id: int):

        client = pymongo.MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")

        db = client["test"]
        collection = db["users"]

        result = collection.delete_one({"_id": delete_id})


        client.close()