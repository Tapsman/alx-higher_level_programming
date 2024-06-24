#!/usr/bin/python3
"""This is a script that will list all the states data base
from the hbtn_0e_0_usa, this time the script lists all the cities
from the hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM
            cities INNER JOIN states ON states.id=cities.state_id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
