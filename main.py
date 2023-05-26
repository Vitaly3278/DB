from create_db import create_db
from register import registration
from verification import verification
from list_db import list_db
from del_users import del_users


def main():


    print('---------MENU-----------')
    print('1. Create DB users')
    print('2. Create users')
    print('3. Verifications')
    print('4. Delete users')
    print('5. List DB')
    print('0. Exit')
    print('------------------------')
    res = int(input('Enter: > '))
    match res:
        case 1:
            create_db()
            main()
        case 2:
            registration()
            main()
        case 3:
            verification()
            main()
        case 4:
            del_users()
            main()
        case 5:
            list_db()
            main()
        case 0:
            exit()

if __name__ == "__main__":
    main()


