#coding=big5
import mysql.connector
from mysql.connector import Error
from datetime import datetime

try:
    #�s��MySQL��Ʈw
    connction = mysql.connector.connect(
        host="192.168.101.65",
        database="weather",
        user="sid001",
        password="lab1209"
    )
    #�R�����    
    cursor = connction.cursor()
    cursor.execute("DELETE FROM th;")

    #�T�{��Ʀ��R��
    connction.commit()

except:
    print("��Ʈw�s������")

finally:
    if(connction.is_connected()):
        cursor.close()
        connction.close()
        print("finished")