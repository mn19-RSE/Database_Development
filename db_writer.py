import sqlite3
import time
import random

# Connect (creates file if it doesn't exist)
conn = sqlite3.connect("test.db")
cur = conn.cursor()

print("Writing data... Ctrl+C to stop")

try:
    while True:
        t = time.time()

        # Fake sensor data
        data = [
            ("temp", 20 + random.uniform(-1, 1)),
            ("pressure", 100 + random.uniform(-2, 2)),
            ("humidity", 45 + random.uniform(-5, 5)),
        ]

        for ch, val in data:
            cur.execute(
                "INSERT INTO measurements VALUES (?, ?, ?)",
                (t, ch, val)
            )

        conn.commit()
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")

conn.close()
