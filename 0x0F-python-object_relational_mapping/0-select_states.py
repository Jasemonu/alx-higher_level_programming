#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa: """

import MySQLdb
import sys


def list_states():
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    db_connect.close()


if __name__ == "__main__":
    list_states()
