#!/usr/bin/python3
"""Cities by states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Connect DB and execute query
        """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    query = '''SELECT cities.id, cities.name, states.name
            FROM states JOIN cities ON states.id = cities.state_id
            ORDER BY cities.id'''
    cur.execute(query)
    cities = cur.fetchall()
    for city in cities:
        print(city)

    cur.close()
    db.close()
