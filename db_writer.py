import sqlite3
import time
import random

# Connect (creates file if it doesn't exist)
conn = sqlite3.connect("test.db")
cur = conn.cursor()

channels = {
    "temp":      ("C", lambda: 20 + random.uniform(-1, 1)),
    "pressure":  ("kPa", lambda: 100 + random.uniform(-2, 2)),
    "humidity":  ("%", lambda: 45 + random.uniform(-5, 5)),
}

print("Writing data... Ctrl+C to stop")

try:
    while True:
        t = time.time()

        for ch, (unit, gen) in channels.items():
            val = gen()
            cur.execute(
                "INSERT INTO measurements (time, channel, value, unit) VALUES (?, ?, ?, ?)",
                (t, ch, val, unit)
            )

        conn.commit()
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")

conn.close()
