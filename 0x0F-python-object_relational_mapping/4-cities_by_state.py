#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306,
                              user=argv[1], passwd=argv[2], db=argv[3])
    cur_db = db_conn.cursor()
    cur_db.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states \
                   ON cities.state_id = states.id \
                   ORDER BY id ASC")
    state_rows = cur_db.fetchall()
    for states in state_rows:
        print(states)
    cur_db.close()
    db_conn.close()
