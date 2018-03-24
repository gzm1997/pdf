import mysql.connector
import os

"""
MYSQL_USER
MYSQL_PASSWORD
"""

class Db(object):
    """docstring for Db"""
    def __init__(self):
        super(Db, self).__init__()
        self.conn = self.get_conn()
    def get_conn(self):
        #environ = os.environ
        MYSQL_USER = "root"
        MYSQL_PASSWORD = "Gzm20125"
        conn = mysql.connector.connect(user = MYSQL_USER, password = MYSQL_PASSWORD)
        return conn





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


db = Db()

if __name__ == "__main__":
    init_db()
        

        
