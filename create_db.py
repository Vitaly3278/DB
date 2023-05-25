import psycopg2
from config import host, user, password, db_name, port


def create_db():


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
            cursor.execute(
                """CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                e_mail varchar(50) NOT NULL,
                password varchar(50) NOT NULL
                );"""
            )
            connection.autocommit = True
            print('[INFO] Table created successfully')

    except Exception as ex:
        print('[INFO] Error while working with PostgreSQL', ex)
    finally:
        if connection:
            connection.close()
            return ('[INFO] PostgreSQL connection close')

#print(create_db())