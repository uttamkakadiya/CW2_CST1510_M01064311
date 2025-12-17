import sqlite3
import pandas as pd
from unicodedata import name
# create user table 

def add_user(conn, name, hash): 
    cursor = conn.cursor()
    sql= (""" INSERT INTO users 
    (username, password_hash) VALUES (?, ?) """)
    param= ('alice', 'hashed_password_123', )
    cursor.execute(sql, param)
    conn.commit() 

def get_all_users(conn):   
    curr = conn.cursor()

    sql = (""" SELECT * FROM users """)

    curr.execute(sql)
    users = curr.fetchall()
    conn.close()
    return users
 
def migrate_users(conn):
    with open("DATA/users.txt", "r") as f:
        users = f.readlines()
    for user in users:
        name, hash = user.strip().split(',')
        add_user(conn, name, hash)
        conn.close()
def migrate_cyber_incidents(conn):
    data1 = pd.read_csv('DATA/cyber_incidents.csv')
    data1.to_sql('cyber_incidents', conn, if_exists='replace', index=False)
    print ('Data Load')

def get_all_user_pandas(conn):
    query = "SELECT * FROM users"
    df = pd.read_sql_query(query, conn)
    return (df)
def migrate_it_tickets(conn):
    data1 = pd.read_csv('DATA/it_tickets.csv')
    conn = sqlite3.connect('DATA/intelligence_platform.db')
    data1.to_sql('it_tickets', conn, if_exists='replace', index=False)
    print ('Data Load')

conn = sqlite3.connect('DATA/intelligence_platform.db')
migrate_it_tickets(conn)

def get_all_cyber_incidents(conn):
    sql = (""" SELECT * FROM cyber_incidents """)
    data = pd.read_sql_query(sql, conn)
    return data





