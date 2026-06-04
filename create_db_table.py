import pymysql
import db_connect2 as dbc

def create_db():
    query = 'create database if not exists akshith_db'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Database created successfully')
        else:
            print('Database already exists')
    except Exception as e:
        print('Error while creating database:', e)

def create_table():
    query = 'create table if not exists employees(id int primary key auto_increment, name varchar(255) not null, designation varchar(255), salary float, phone_number bigint unique)'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Table created successfully')
        else:
            print('Table already exists')
    except Exception as e:
        print('Error while creating table:', e)

create_db()
create_table()