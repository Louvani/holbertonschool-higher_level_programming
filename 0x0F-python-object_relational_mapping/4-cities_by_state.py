#!/usr/bin/python3
'''Module that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument. '''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT cities.id, cities.name, states.name\
        FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
