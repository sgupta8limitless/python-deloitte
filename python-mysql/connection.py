import mysql.connector

class Connection:
    def __init__(self):
        self.__db=mysql.connector.connect(host="localhost",port="3307",user="root",password="thorabh8",database="inventory")
        self.__cursor=self.__db.cursor()

    def getDb(self):
        return self.__db

    def getCursor(self):
        return self.__cursor
        