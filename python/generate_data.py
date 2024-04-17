from faker import Faker
import json

# On instancie la bibliothèque Faker
fake = Faker()

def generate_data(nb_person: int):

        #On génère un tableau qui contiendra nos différents faux-utilisateurs
        data = []

        #On crée un nombre de données correspondant au paramètre de la fonction qui sera donné par une entrée utilisateur dans main.py
        for _ in range(nb_person):
                nom = fake.name()
                email = nom.replace(" ",".").lower() + "gmail.com"

                #On crée un dictionnaire pour obtenir la syntaxe d'un fichier json
                data_dict = {
                        'nom': nom,
                        'age': fake.random_int(min=18, max=90),
                        'email': email,
                        'created_at': fake.date_time_this_decade(tzinfo=None).isoformat()
                }

                # On ajoute le dictionnaire récemment crée dans le tableau
                data.append(data_dict)

        # On écrit les données du tableau dans un fichier nommé 'data.json'
        with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
