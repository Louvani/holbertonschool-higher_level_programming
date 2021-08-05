#!/usr/bin/python3
'''Module to  lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa'''

import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                            passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
# HERE I have to know SQL to grab all states in my database
cur.execute("SELECT * FROM states WHERE name regexp '^N.' ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
        print(row)
cur.close()
conn.close()
