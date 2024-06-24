#!/usr/bin/python3
"""This is a script that will list all the states data base
from the hbtn_0e_0_usa, this time the script takes an argument and
displays all the values in the states table of hbtn_0e_0_usa.
but this time it is safe from MySQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
