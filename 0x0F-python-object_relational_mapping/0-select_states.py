#!/usr/bin/python3
"""
This is a script that lists all the states from the
database called hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in row:
        print(row)
    c.close()
    db.close()
