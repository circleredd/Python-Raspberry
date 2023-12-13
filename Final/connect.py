#coding=big5
import mysql.connector
from mysql.connector import Error

try:
    #連接MySQL資料庫
    connction = mysql.connector.connect(
        host="192.168.101.65",
        database="weather",
        user="sid001",
        password="lab1209"
    )
    if connction.is_connected():
        #顯示資料庫版本
        db_Info = connction.get_server_info()
        print("資料庫版本", db_Info)

        #顯示目前使用的資料庫
        cursor = connction.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫:", record)

except:
    print("資料庫連接失敗")

finally:
    if(connction.is_connected()):
        cursor.close()
        connction.close()
        print("資料庫連線已關閉")