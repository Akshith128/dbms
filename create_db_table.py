import pymysql
import db_connect2 as dbc2

def create_db():
    query = "CREATE DATABASE IF NOT EXISTS akshith_db"

    try:
        connection = dbc2.db_connect()

        cursor = connection.cursor()
        cursor.execute(query)

        connection.commit()
        cursor.close()
        dbc2.db_disconnect(connection)

        print("Database created")

    except Exception as e:
        print("DB creation failed", e)

def create_table():
    query = 'create table if not exists emp(id int primary key auto_increment, name varchar(20), age int, salary float, phone bigint unique)'
    try:
        connection = dbc2.db_connect_server()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Table created')
        else:
            print('Table already exists')

    except Exception as e:
        print('Table creation failed', e)

create_db()
create_table()