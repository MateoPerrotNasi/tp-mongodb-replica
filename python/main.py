import generate_data
import import_data
import update_data
import delete_data

if __name__ == "__main__":

        # On demande à l'utilisateur quel script il voudrait lancer
        print(" 1-Generate data")
        print(" 2-Insert data")
        print(" 3-Update data")
        print(" 4-Delete data")
        choice = int(input("Which script would you like to execute?\n"))

        # On lance le script en fonction de son choix
        match choice:
                case 1:
                        nb_person = int(input("How many person would you like to generate\n"))
                        generate_data.generate_data(nb_person)
                case 2:
                        import_data.import_data()
                case 3:
                        update_data.update_data()
                case 4:
                        delete_id = int(input("Insert the id you want to delete\n"))
                        delete_data.delete_data(delete_id)
