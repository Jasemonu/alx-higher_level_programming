#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb
import sys


def safe_from_sql_injection():
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        )
    db_cursor = db_connect.cursor()
    query = """SELECT * FROM states ORDER BY id ASC"""
    db_cursor.execute(query)
    states = db_cursor.fetchall()
    for state in states:
        if (state[1] == sys.argv[4]):
            print(state)
    db_cursor.close()
    db_connect.close()


if __name__ == "__main__":
    safe_from_sql_injection()
