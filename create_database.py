import sqlite3

def create_db ():
    con = sqlite3.connect('clinic.db')
    cur = con.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS xrays(address text, contact text, price text, state text, date text, age text, gender text, name text, xid INTEGER PRIMARY KEY AUTOINCREMENT)")
    con.commit()

create_db()