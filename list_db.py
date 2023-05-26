import psycopg2
from config import host, user, password


def list_db():
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
            # Выборка всех пользователей
            select_query = "SELECT * from users"

            # item_tuple = (user_mail, user_password)
            cursor.execute(select_query)

            for person in cursor.fetchall():
                print(f'ID = {person[0]}\nFirst name = {person[1]}\n'
                      f'Last name = {person[2]}\ne-mail = {person[3]}\npassword = {person[4]}')
                print('-' * 45)

    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection close')
