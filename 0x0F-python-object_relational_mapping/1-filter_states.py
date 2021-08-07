#!/usr/bin/python3
'''
Module to  lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':

    connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connect.cursor()
    query = "SELECT * FROM states\
        WHERE name LIKE BINARY 'N%'\
        ORDER BY id ASC"
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connect.close()
