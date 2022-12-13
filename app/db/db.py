import sqlite3

def get_connection():
    conn = sqlite3.connect("app/db/db")
    return conn


def query_db(query, args=(), all=False):
    conn = get_connection()

    with conn:
        cur = conn.cursor()
        r = cur.execute(query, args)
        r = cur.fetchall()
    conn.close()

    return (r[0] if r else None) if not all else r