import psycopg2
from config import host, user, password


def create_db():
    try:
        # Соединение с базой данных

        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password
        )

        # Создание обьекта Курсор
        with connection.cursor() as cursor:
            # Создание таблицы users
            cursor.execute(
                """CREATE TABLE users(
                id serial PRIMARY KEY,
                e_mail varchar(50) NOT NULL,
                password varchar(50) NOT NULL
                );"""
            )
            connection.autocommit = True
            print('[INFO] Table created successfully')

    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        print ('[INFO] PostgreSQL connection close')
