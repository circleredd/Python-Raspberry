#coding=big5
import mysql.connector
from mysql.connector import Error
from datetime import datetime

try:
    #連接MySQL資料庫
    connction = mysql.connector.connect(
        host="192.168.101.65",
        database="weather",
        user="sid001",
        password="lab1209"
    )
    #刪除資料    
    cursor = connction.cursor()
    cursor.execute("DELETE FROM th;")

    #確認資料有刪除
    connction.commit()

except:
    print("資料庫連接失敗")

finally:
    if(connction.is_connected()):
        cursor.close()
        connction.close()
        print("finished")