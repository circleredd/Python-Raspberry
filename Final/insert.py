#coding=big5
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import time
import random

try:
    #連接MySQL資料庫
    connction = mysql.connector.connect(
        host="192.168.101.65",
        database="weather",
        user="sid001",
        password="lab1209"
    )
    #新增資料
    count = 1
    while(True):
        sql = "INSERT INTO th(siteid, gettime, temp, humi) VALUES (%s, %s, %s, %s);"
        new_data = (str(random.randint(1, 5)).zfill(3), datetime.now(), round(random.uniform(18.5, 20), 2), round(random.uniform(75, 85), 2))   #id, time, temp, humi
        cursor = connction.cursor()
        cursor.execute(sql, new_data)        
        print("date ->", count)
        count += 1
        if count > 100:
            break
        time.sleep(5)
        

    #確認資料有存入資料庫
    connction.commit()

except:
    print("資料庫連接失敗")

finally:
    if(connction.is_connected()):
        cursor.close()
        connction.close()
        print("finished")