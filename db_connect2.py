import pymysql

def db_connect_server():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='akshith',
            password='akki8877',
            port=3306,
            charset='utf8'
        )
        print("Server connected")
        return connection
    except Exception as e:
        print("Server connection failed")
        print(e)
        return None


def db_connect():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='akshith',
            password='akki8877',
            port=3306,
            database='akshith_db',
            charset='utf8'
        )
        print("DB connected")
        return connection
    except Exception as e:
        print("DB connection failed")
        print(e)
        return None


def db_disconnect(connection):
    connection.close()
    print("DB disconnected")