#!/usr/bin/python3
"""deletes whole table"""


import MySQLdb
import sys


if __name__ == "__main__":
    search_name = sys.argv[4]
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    cur = conn.cursor()
    query = ("SELECT * FROM states \
            WHERE BINARY name=%s  \
            ORDER BY id ASC")
    cur.execute(query, (search_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
