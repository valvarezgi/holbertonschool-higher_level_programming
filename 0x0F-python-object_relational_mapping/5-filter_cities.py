#!/usr/bin/python3
""" All cities by state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    query = '''SELECT cities.name FROM cities
            JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id'''
    cur.execute(query, (argv[4],))
    cities = cur.fetchall()
    if len(cities):
        for idx in range(0, len(cities)):
            print(cities[idx][0], end=', ' if idx != len(cities) - 1 else '\n')
    else:
        print('')

    cur.close()
    db.close()
