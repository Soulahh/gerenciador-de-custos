import sqlite3

def criar_database():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS despesas(ID integer PRIMARY KEY AUTOINCREMENT, descricao VARCHAR(255) NOT NULL, valor DECIMAL(10,2) NOT NULL, data DATE NOT NULL);''')
    con.commit()


def get_connection():
    return sqlite3.connect('database.db')
criar_database()