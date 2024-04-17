# tp-mongodb-replica

## Comment démarrer le replica set:
Une fois le répertoire téléchargé, rendez vous dans le dossier docker-compose.
Ouvrez le terminal de commande et entrez ceci:
`docker-compose up -d`
Cela lancera les 3 conteneurs en fond, vous n'aurez ensuite qu'à effectuer la commande:
`docker exec -it mongo1 bash`
Et vous voila dans le cli docker ! Pour choisir le conteneur sur lequel vous connecter, changer `mongo1` en `mongo2` ou `mongo3`.


En allant dans le cli mongodb à l'aide de la commande:
`mongosh`
Vous pourrez créer des données et constater qu'elles se répliquent.

## Comment générer et insérer des données:
La prochaine étape vous demandera de copier les fichier contenus dans le dossier "python" à l'intérieur du conteneur.
Une fois fait, lancez le fichier `main.py` avec la commande:
`python3 main.py`
Vous pourrez ensuite choisir quelle action effectuée entre:
- Générer des données
- Insérer des données
- Modifier des données
- Supprimer des données

## Les commandes CLI pour les opérations CRUD:
Lorsque vous êtes connectés dans le cli mongodb, vous pouvez effectuer ces commandes:

### Create
`users.insertOne({"key": "value"})`
Remplacez `key` et `value`par les valeurs que vous souhaitez.

### Read
`users.find()`

### Update
`users.updateMany({"$operator" : {"key" : "value"})`
A noter que la variable `$operator` correspond à certains paramètres prédéfinis dans la documentation tel que `$inc` pour l'incrémentation ou `$set` pour redéfinir une valeur.

### Delete
`users.deleteOne({"key": "value"})`
Le paramètre passé dans la fonction correspond au filtre

## Différence entre CRUD et script:
Aucune grande différence n'a été observée si ce n'est que les fonctions ne sont pas écrites en camelCase (CRUD) mais en snake_case (script).

## Difficultes rencontrées
La principale difficulté rencontrée a été l'execution des scripts pythons. En effet il a été nécessaire de copier les fichiers pythons à l'intérieur du docker afin de pouvoir les executer, hors du conteneur la liaison entre python et mongodb ne s'effectuait pas.

J'ai également rencontré une autre difficulté, lors de l'étape d'insertion des fausses données générée dans un json, j'ai récupéré un code python se trouvant dans la documentation pour [insérer les données d'un fichier json dans mongodb à l'aide de python](https://www.mongodb.com/compatibility/json-to-mongodb). Le code en question ne fonctionnait pas et après avoir cherché en ligne il semblerait que le code préscrit soit erronné.