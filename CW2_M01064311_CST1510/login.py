import bcrypt
import os
def hash_password(password):
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(binary_password, salt)
    return hashed.decode('utf-8')

def validate_password(password, hashed):
    """Return True if password matches the stored hashed password (both strings)."""
    psw = password.encode('utf-8')
    hash_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(psw, hash_bytes)

def register_user():
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    hashed = hash_password(user_password)
    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{user_name},{hashed}\n")
    print("User registered successfully.")

def login_user():
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    if not os.path.exists("users.txt"):
        print("No users registered yet.")
        return False
    with open("users.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            name, stored_hash = line.split(',', 1)
        except ValueError:
            # malformed line, skip
            continue
        # debug: print(f'name = {name}, hash = {stored_hash}')
        if name == user_name:
            return validate_password(user_password, stored_hash)
    return False

def menu():
    print("welcome to the user system")
    print("choose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            register_user()
            print("Registration successful.")
        elif choice == '2':
            if login_user():
                print("Login successful.")
            else:
                print("Login failed.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()



