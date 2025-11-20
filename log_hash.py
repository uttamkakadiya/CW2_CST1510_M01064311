import bcrypt
import sqlite3


def put_it_in_the_database(sql, param):
    conn = sqlite3.connect("DATA\\itelligence_platform.db")
    curr = conn.cursor()
    curr.execute(sql, param)
    conn.commit()
    conn.close()

def hash_password(password):
    binery_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(binery_password, salt)
    return hash.decode('utf-8')


def valid_hash(password, hash):    
    bin_pwd = password.encode('utf-8')
    bin_hash = hash.encode('utf-8')
    return bcrypt.checkpw(bin_pwd, bin_hash)

def register_user():
    user_name = input('Enter your user name: ')
    user_pwd = input('Enter your password: ')
    hash = hash_password(user_pwd)
    with open('user.txt','a')as f:
         f.write(f'{user_name},{hash}\n')

def register_user_db():
    user_name = input('Enter your user name: ')
    user_pwd = input('Enter your password: ')
    hash = hash_password(user_pwd)
    sql = """INSERT INTO users (username, password_hash) VALUES (?, ?)"""
    param = (user_name, user_pwd)
    put_it_in_the_database(sql, param)

def log_in_user():
    user_name = input('Enter your user name: ')
    user_pwd = input('Enter your password: ')
    with open('user.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        name, hash = user.strip().split(',')
    
    if user_name == name:
        return valid_hash(user_pwd, hash)
    return False