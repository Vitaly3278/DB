# DB
Создание таблицы пользователей:
CREATE TABLE users(
                id serial PRIMARY KEY,
                first_name varchar(50) NOT NULL,
                last_name varchar(50) NOT NULL,
                e_mail varchar(50) NOT NULL,
                password varchar(50) NOT NULL
                );
 
 Данные для соединения с базой находятся в файле config.py
 
