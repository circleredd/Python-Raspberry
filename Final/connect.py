#coding=big5
import mysql.connector
from mysql.connector import Error

try:
    #�s��MySQL��Ʈw
    connction = mysql.connector.connect(
        host="192.168.101.65",
        database="weather",
        user="sid001",
        password="lab1209"
    )
    if connction.is_connected():
        #��ܸ�Ʈw����
        db_Info = connction.get_server_info()
        print("��Ʈw����", db_Info)

        #��ܥثe�ϥΪ���Ʈw
        cursor = connction.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("�ثe�ϥΪ���Ʈw:", record)

except:
    print("��Ʈw�s������")

finally:
    if(connction.is_connected()):
        cursor.close()
        connction.close()
        print("��Ʈw�s�u�w����")