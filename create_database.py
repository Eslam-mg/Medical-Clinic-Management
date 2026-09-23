import sqlite3

def create_db():
    con = sqlite3.connect('clinic.db')

    con.execute("""
        CREATE TABLE IF NOT EXISTS xrays(
            address TEXT,
            contact TEXT,
            price REAL,
            state TEXT,
            date TEXT,
            age INTEGER,
            gender TEXT,
            name TEXT,
            xid INTEGER PRIMARY KEY AUTOINCREMENT
        )
    """)

    con.commit()
    con.close()


if __name__ == "__main__":
    create_db()