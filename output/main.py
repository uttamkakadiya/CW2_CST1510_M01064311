import bcrypt

password = 'Magic123'

def hash_password(password):
    binery_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(binery_password,salt)
    return hash.decode('utf-8')

password = 'Magic123'
print('Hashpassword -> ',hash_password(password))