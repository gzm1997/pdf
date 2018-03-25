# _*_ coding: utf-8 _*_
import mysql.connector
import os
#Db对象，内含一个mysql连接
class Db(object):
    """docstring for Db"""
    def __init__(self):
        super(Db, self).__init__()
        self.conn = self.get_conn()
    def get_conn(self):
        #environ = os.environ
        #MYSQL_USER = os.environ["MYSQL_USER"]
        #MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
        MYSQL_USER = "root"
        MYSQL_PASSWORD = "Gzm20125"
        conn = mysql.connector.connect(user = MYSQL_USER, password = MYSQL_PASSWORD)
        return conn
#初始化数据库
def init_db():
    db = Db()
    conn = db.conn
    cursor = conn.cursor()
    cursor.execute("create database if not exists pdf;")
    cursor.execute("use pdf;")
    cursor.execute("\
        CREATE TABLE if not exists File( \
            name varchar(50) not null, \
            content mediumblob, \
            primary key (name) \
        ); \
    ")
    conn.commit()
    cursor.close()
#声明一个Db实例
db = Db()

if __name__ == "__main__":
    init_db()
        

        
