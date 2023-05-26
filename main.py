from create_db import create_db
from register import registration
from verification import verification
from list_db import list_db
print('---------MENU-----------')
print('1. Create DB users')
print('2. Create users')
print('3. Verifications')
print('4. Delete users')
print('5. List DB')
print('------------------------')
res = int(input('Enter: > '))
match res:
    case 1:
        create_db()
    case 2:
        registration()
    case 3:
        verification()
    case 4:
        pass
    case 5:
        list_db()


