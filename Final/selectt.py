#coding=big5
import mysql.connector
from mysql.connector import Error

try:
    #�s��MySQL��Ʈw
    connction = mysql.connector.connect(
        host="192.168.28.65",
        database="weather",
        user="sid001",
        password="lab1209"
    )
    #�d�߸�Ʈw
    cursor = connction.cursor()
    cursor.execute("SELECT siteid, gettime, temp, humi FROM th;")

    for(siteid, gettime, temp, humi) in cursor:
        print("SiteID: %s, GetDateTime: %s, Temperature: %s, Humidity: %s" %(siteid, gettime, temp, humi))

except:
    print("��Ʈw�s������")

finally:
    if(connction.is_connected()):
        cursor.close()
        connction.close()
        print("��Ʈw�s�u�w����")