import mysql.connector
from mysql.connector import Error


try:
    #連接MySQL資料庫
    connection = mysql.connector.connect(
        host="192.168.101.65",
        database="weather",
        user="sid001",
        password="lab1209"
    )
    if connection.is_connected():
        #顯示資料庫版本
        db_Info = connection.get_server_info()
        print("資料庫版本", db_Info)

        #顯示目前使用的資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫:", record)

except:
    print("資料庫連接失敗")
    
