#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    cur = db.cursor()

    # Exécution de la requête SQL avec un filtre
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
