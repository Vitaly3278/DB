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

            postgresql_select_query = "select * from users where e_mail=%s and password = %s"

            cursor.execute(postgresql_select_query, (user_e_mail, user_password))
            mobile_records = cursor.fetchall()
            if len(mobile_records) >0:
                for row in mobile_records:
                    print(row)
            else:
                print('[INFO] NOT FOUND')


    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
