#!/usr/bin/python3
'''
Module that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':

    connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connect.cursor()

    query = "SELECT * FROM states WHERE name LIKE '{}'\
        ORDER BY id ASC".format(argv[4])

    cursor.execute(query)

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connect.close()
