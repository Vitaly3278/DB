import psycopg2
from config import host, user, password


def del_users():
    print('=' * 20)
    user_e_mail = input('INPUT DELETED E-mail: > ')
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
            # Удаление пользователя по e-mail

            postgresql_delete_query = "DELETE FROM users WHERE e_mail=%s"

            cursor.execute(postgresql_delete_query, (user_e_mail,))
            count = cursor.rowcount
            print(f'[INFO] {count} USER {user_e_mail} DELETED')

    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        print('[INFO] PostgreSQL connection close')
