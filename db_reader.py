# May no longer work with added db info

import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("""
    SELECT value
    FROM measurements
    WHERE channel = ?
    ORDER BY time DESC
    LIMIT 1
""", ("temp",))

row = cur.fetchone()

print("Latest temp:", row[0])

conn.close()
