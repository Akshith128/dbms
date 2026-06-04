import pymysql
connection = pymysql.connect(user = 'akshith' , password = 'akki8877' , port = 3306 , database = 'airlinedb' , charset = 'utf8' , host = 'localhost')

print('DB Connected')
connection.close()
print('DB Disconnected')
