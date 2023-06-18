#!/usr/bin/python3
"""
A script that takes in the name of a state
as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def search_city():
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        )
    db_cursor = db_connect.cursor()
    query = """
                SELECT * FROM cities INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC
            """
    db_cursor.execute(query)
    cities = db_cursor.fetchall()
    search_city = ''
    for city in cities:
        if (city[4] == sys.argv[4]):
            search_city += city[2] + ', '
    print(search_city[0:-2:])
    db_cursor.close()
    db_connect.close()


if __name__ == "__main__":
    search_city()
