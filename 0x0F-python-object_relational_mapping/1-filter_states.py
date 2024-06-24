#!/usr/bin/python3
"""This is a script that will list all the states data base
from the hbtn_0e_0_usa, this time the script lists all names starting
with a name starting with N from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER By states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
