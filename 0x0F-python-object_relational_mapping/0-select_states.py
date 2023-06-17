#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa: """

import MySQLdb
import sys


def list_states(username, password, database):
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    db_connect.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states()
