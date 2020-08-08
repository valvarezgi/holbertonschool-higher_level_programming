#!/usr/bin/python3
"""SQL injection"""

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
    query = "SELECT * FROM states  WHERE name = %s ORDER BY id"
    cur.execute(query, (argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
