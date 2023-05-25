import psycopg2

if connection:
    connection.close()
    print('[INFO] PostgreSQL connection close')