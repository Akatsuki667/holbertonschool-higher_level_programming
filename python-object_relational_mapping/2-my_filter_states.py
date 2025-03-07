#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the argument
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    cur = db.cursor()

    # Exécution de la requête SQL avec format (ATTENTION : vulnérable à l'injection SQL)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
