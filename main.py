from log_hash import register_user, log_in_user

def menu():
    print('*'*30)
    print('*** Welcome to my system ***')
    print('Choose frome the following option :')
    print(' 1. Register\n 2. Login\n 3. Exit')
    print('*'*30)

def main():
    while True:
        menu()
        choice = input('> ')
        if choice =='1':
            register_user()
        elif choice == '2':
            if log_in_user():
                print('You logged in Successfully')
            else:
                print('Incorrect Login')
        elif choice == '3':
            print('Good Bye!!')
            break

if __name__ == '__main__':
    main()