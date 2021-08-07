#!/usr/bin/python3
'''
Module to select states from hbtn_0e_0_usa DataBase
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connect = MySQLdb.connect(host="localhost", user=argv[1],
                              passwd=argv[2], db=argv[3], port=3306)
    cursor = connect.cursor()
    query = "SELECT * FROM states ORDER BY 'states.id' ASC"
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connect.close()
