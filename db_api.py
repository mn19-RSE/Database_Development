from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3

DB = "test.db"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/value"):
            # Example: /value?ch=temp
            ch = self.path.split("ch=")[-1]

            conn = sqlite3.connect(DB)
            cur = conn.cursor()
            cur.execute(
                "SELECT value FROM measurements WHERE channel=? ORDER BY time DESC LIMIT 1",
                (ch,)
            )
            row = cur.fetchone()
            conn.close()

            value = row[0] if row else "NaN"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(str(value).encode())

        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
