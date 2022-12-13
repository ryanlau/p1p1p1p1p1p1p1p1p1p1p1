import sqlite3

def establishConnection():
    DB_FILE="app/db/db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    return (c, db)

def disconnect(db):
    db.commit() #save changes
    db.close()  #close database


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