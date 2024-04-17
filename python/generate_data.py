from faker import Faker
import json

fake = Faker()

def generate_data(nb_person: int):
        data = []
        for _ in range(nb_person):
                nom = fake.name()
                email = nom.replace(" ",".").lower() + "gmail.com"
                data_dict = {
                        'nom': nom,
                        'age': fake.random_int(min=18, max=90),
                        'email': email,
                        'created_at': fake.date_time_this_decade(tzinfo=None).isoformat()
                }
                data.append(data_dict)


        with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
