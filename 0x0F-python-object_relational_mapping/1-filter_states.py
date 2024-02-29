#!/usr/bin/python3
"""shows all content of a table in a database with letter N"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM states \
            WHERE BINARY name LIKE 'N%' \
            ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
