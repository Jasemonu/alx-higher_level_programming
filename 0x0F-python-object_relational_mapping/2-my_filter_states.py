#!/usr/bin/python3
"""
A script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys


def search_states():
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    db_cursor = db_connect.cursor()
    db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(argv[4]))
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    db_connect.close()


if __name__ == "__main__":
    search_states()
