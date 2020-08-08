#!/usr/bin/python3
"""Get all states"""

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
cur.execute("SELECT * FROM states ORDER BY id")
states = cur.fetchall()
for state in states:
    print(state)

cur.close()
db.close()
