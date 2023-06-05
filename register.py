import psycopg2
from config import host, user, password, db_name, port


def registration():
    print('=' * 25)
    # user_first_name = input('First name: > ')
    # user_last_name = input('Last name: > ')
    user_mail = input('E-mail: > ')
    user_password = input('Password: > ')

    try:
        # Соединение с базой данных

        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )

        # Создание обьекта Курсор
        with connection.cursor() as cursor:
            connection.autocommit = True
            # Регистрация нового пользователя
            insert_query = """INSERT INTO users(e_mail, password)
                                          VALUES (%s, %s)"""

            item_tuple = (user_mail, user_password)
            cursor.execute(insert_query, item_tuple)

            print('[INFO] USER created successfully')

    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        print('[INFO] PostgreSQL connection close')



