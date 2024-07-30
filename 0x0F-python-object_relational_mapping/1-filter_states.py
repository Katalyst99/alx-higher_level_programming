#!/usr/bin/python3
"""A script that lists states with a name starting with N from the db"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306,
                              user=argv[1], passwd=argv[2], db=argv[3])
    cur_db = db_conn.cursor()
    cur_db.execute("SELECT * \
            FROM states \
            WHERE name LIKE BINARY 'N%'")
    state_rows = cur_db.fetchall()
    for states in state_rows:
        print(states)
    cur_db.close()
    db_conn.close()
