import pymysql

def db_connect():
    connection = None
    try:
        connection = pymysql.connect(user='akshith', password='akki8877', port=3306, database='airlinedb', charset='utf8', host='localhost')
        print('DB Connected')
    except Exception as e:
        print("DB connection failed")
    return connection

def db_disconnect(connection):
    try:
        connection.close()
        print('DB Disconnected')
    except:
        print("DB disconnection failed")

connection = db_connect() 
db_disconnect(connection)