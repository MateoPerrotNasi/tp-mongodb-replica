import pymongo

def delete_data(delete_id: int):

        # On se connecte à mongodb
        client = pymongo.MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")

        # On instancie de la db et de la collection utilisés
        db = client["test"]
        collection = db["users"]

        # On effectue une resquête pour supprimer l'élément de la collection correspondant à l'id
        result = collection.delete_one({"_id": delete_id})

        # On arrête la connexion avec mongodb
        client.close()