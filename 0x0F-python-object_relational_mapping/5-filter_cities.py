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
    query = ("SELECT cities.name \
            FROM cities, states \
            WHERE cities.state_id = states.id \
            AND states.name = %s;")
    cur.execute(query, (search_name,))
    query_rows = cur.fetchall()
    query_rows = [row[0] for row in query_rows]
    print(", ".join(query_rows))
    cur.close()
    conn.close()
