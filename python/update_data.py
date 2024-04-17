import pymongo

def update_age():

        # On se connecte à mongodb
        client = pymongo.MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")

        # On instancie de la db et de la collection utilisés
        db = client["test"]
        collection = db["users"]

        # On effectue la requête demandant à tous les contacts de la table users de d'augmenter la valeur "age" de 5
        resultat = collection.update_many({},{"$inc": {"age": 5}})

        # On arrête la connexion avec mongodb
        client.close
