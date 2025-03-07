#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the argument (safe from SQL injection)
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name>
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

    # Exécution de la requête SQL en utilisant une requête paramétrée (évite l'injection SQL)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
