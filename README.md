# PureBeurre
OpenclassRooms projet5

Programme tournant sur un serveur MySQL, codé en Python 3.7 en environnement virtuel.
Avant de lancer le programme, il faut installer "requirements.txt".
Le programme est composé de différents modules sur deux dossiers, "data" et "body".

Le module data contiens, 4 sous modules :
- dowload_products (qui se charge de se connecter à l’Api OPENFOODFACTS, et de préparer les données a être insérées dans la Base de données.
- clear-data (qui vas donc « parser », et garder seulement les données requises pour le fonctionnement de l’application, ainsi que préparer les données afin de procéder a l’insertion dans la différentes tables de la base de données)
- insert_data (vas gérer l’insertion des données dans la base de données)
- models (quant à lui, vas mettre en place et créer les différentes tables et s’occuper des différentes requêtes par l’utilisation de l’ORM peewee)

Le module body contient 7 sous-modules :
- first (c’est le menu principal)
- meeting_user (première fenêtre afin de renseigner son nom et faire connaiscance)
- choice_cat (permettra de choisir et valider une classe de produits parmi les classes proposées)
- product_choice (pour choisir un produit en entrant son numéro, l’utilisateur se verra proposer des paquets de 25 produits)
- proposed_products (pour afficher les données du produit choisi, ainsi que proposer le produit de substitution, l’utilisateur pourra voir leur pas internet sur le site d’Openfoodfacts, et enregistrer son choix ainsi que le produit proposé)
- save_choice (permets d’enregistrer le choix dans la base de données afin que l’utilisateur puisse les consultera tout moment)
- consult_rec (vas afficher la liste de produits enregistrés par l’utilisateur)

Le programe se lance par le module "main.py".
Lors de la premiére utilisation, on rengtre son nom, et au menu on choisi l'option 4 - "premiére utilisation", et suivez les instructions.

