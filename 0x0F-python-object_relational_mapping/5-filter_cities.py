#!/usr/bin/python3
"""A script that takes in the name of a state as an arg and lists all cities"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", port=3306,
                              user=argv[1], passwd=argv[2], db=argv[3])
    cur_db = db_conn.cursor()
    cur_db.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states \
                   ON cities.state_id = states.id \
                   WHERE states.name=%s \
                   ORDER BY id ASC", (argv[4],))
    state_rows = cur_db.fetchall()
    print(', '.join([city[1] for city in state_rows]))
    cur_db.close()
    db_conn.close()
