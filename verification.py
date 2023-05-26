import psycopg2
from config import host, user, password

def verification():
    print('=' * 20)
    user_e_mail = input('E-mail: > ')
    user_password = input('Password: > ')

    try:
        # Соединение с базой данных

        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password

        )

        # Создание обьекта Курсор
        with connection.cursor() as cursor:
            connection.autocommit = True
            # Регистрация нового пользователя
            select_query = "SELECT e_mail, password from users"

            # item_tuple = (user_mail, user_password)
            cursor.execute(select_query)

            for person in cursor.fetchall():
                print(f"{person[0]} - {person[1]}")

    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
