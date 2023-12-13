from link import *


class DB():
    def connect():
        cursor = connection.cursor()
        return cursor
    
    def execute(cursor, sql):
        cursor.execute(sql)
        return cursor
    
    def execute_input(cursor, input):
        cursor.execute(None, input)
        return cursor
    
    def fetchall(cursor):
        return cursor.fetchall()
    

class Time():
    def get_time(date):
        sql = 'SELECT time FROM door WHERE YEAR(time) = %s AND MONTH(time) = %s AND DAY(time) = %s' %(date[0], date[1], date[2])
        return DB.fetchall(DB.execute(DB.connect(), sql))