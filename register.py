import psycopg2
from config import host, user, password, db_name, port


def registration():
    print('=' * 20)
    # f_name = input('First name: > ')
    # l_name = input('Last name: > ')
    # mail = input('E-mail: > ')
    # pas = input('Password: > ')

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
            f_name = input('First name: > ')
            l_name = input('Last name: > ')
            mail = input('E-mail: > ')
            pas = input('Password: > ')
            cursor.execute(""" INSERT INTO users(first_name, last_name, e_mail, password) 
            VALUES (f_name, l_name, mail, pas);"""
                           )

            print('[INFO] USER created successfully')

    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')


registration()
