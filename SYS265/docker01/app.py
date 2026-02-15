from flask import Flask, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visitors (name TEXT);")
    conn.commit()

    name = request.args.get('name')
    if name:
        cur.execute("INSERT INTO visitors (name) VALUES (%s);", (name,))
        conn.commit()

    cur.execute("SELECT name FROM visitors;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return str([r[0] for r in rows])

app.run(host="0.0.0.0", port=5000)

