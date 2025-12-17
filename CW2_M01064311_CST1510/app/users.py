import os 
import pandas as pd
import bcrypt

def is_valid_hash(psw, hash):
    """Check if a password matches a bcrypt hash."""
    hash_ = hash.encode('utf-8')
    byte_psw = psw.encode('utf-8')
    is_valid = bcrypt.checkpw(byte_psw, hash_)
    return is_valid

def hash_password(password: str) -> str:
    "Hash a password for storing."
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verify a stored password against one provided by user""" 
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def set_user(conn,name,hash):
    curr = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash) VALUES (?, ?)""")
    param = (name,hash)
    curr.execute(sql, param)
    conn.commit()

def get_all_users(conn):
    curr = conn.cursor()
    sql = (""" SELECT * FROM users """)
    curr.execute(sql)
    all_users = curr.fetchall()
    for i in all_users:
        print(i)

def get_one_user(conn, name_):
    curr = conn.cursor()
    sql = (""" SELECT * FROM users WHERE username = ? """)
    param = (name_,)
    curr.execute(sql, param)
    user = curr.fetchone()
    conn.close()
    return user

def update_user_password(conn, name_, new_hashed_password):
    curr = conn.cursor()
    sql = (""" UPDATE users SET password_hash = ? WHERE username = ? """)
    param = (new_hashed_password, name_)
    curr.execute(sql, param)
    conn.commit()

def delete_user(conn, user_name):
    curr = conn.cursor()
    sql = (""" DELETE FROM users WHERE username = ? """)
    param = (user_name,)
    curr.execute(sql, param)
    conn.commit()
    print(f"User {user_name} deleted successfully.")

def migrate_user(conn):
    with open("Data/users.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        name, hash = line.strip().split(",")
        set_user(conn, name, hash)
        conn.close() 
    

    

def user_registration(conn):
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    hashed = hash_password(user_password)
    set_user(conn,user_name, hashed)
    print("User registered successfully.")

def user_login(conn):
    name = input("Enter username: ")
    password = input("Enter password: ")
    id,name_db, hash_db = get_one_user(conn, name)
    if name == name_db:
        return verify_password(hash_db, password)
    return False