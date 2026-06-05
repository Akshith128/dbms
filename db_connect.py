import pymysql

try:
    connection = pymysql.connect(
        user='akshith',
        password='akki8877',
        port=3306,
        database='akshith_db',
        charset='utf8',
        host='localhost'
    )

    print('DB connected')

    connection.close()
    print('DB disconnected')

except Exception as e:
    print("Connection failed")
    print(e)