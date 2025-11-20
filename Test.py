import sqlite3
import pandas as pd
conn = sqlite3.connect("DATA\\itelligence_platform.db")

def create_user_table(conn):
    curr = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            )"""
    curr.execute(sql)
    conn.commit()

# Create table
create_user_table(conn)

# Insert user
curr = conn.cursor()
sql = """INSERT INTO users (username, password_hash) VALUES (?, ?)"""
param = ('anna', 'hash1234')
curr.execute(sql, param)
conn.commit()
conn.close()

# Fetch users
conn = sqlite3.connect("DATA\\itelligence_platform.db")
curr = conn.cursor()

sql = "SELECT * FROM users"
curr.execute(sql)
users = curr.fetchall()
conn.close()

def migrate_it_tickets(conn):
    data1 = pd.read_csv()