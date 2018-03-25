# _*_ coding: utf-8 _*_
import pdf.db as db
#文件对象
class File(db.Db):
    """docstring for File"""
    def __init__(self, name, content):
        super(File, self).__init__()
        self.__name = name
        self.__content = content
    @property
    def name(self):
        return self.__name
    @property
    def content(self):
        return self.__content
    #将文件对象保存到数据库中
    def save(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("use pdf;")
            cursor.execute("insert into File(name, content) value(%s, %s);", [self.__name, self.__content])
            self.conn.commit()
            cursor.close()
        except Exception as e:
            return False
        else:
            return True
    #更新
    def update(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("use pdf;")
            cursor.execute("update File set content = %s where name = %s;", [self.__content, self.__name])
            self.conn.commit()
            cursor.close()
        except Exception as e:
            return False
        else:
            return True
    #从数据库中按照文件名删除文件
    @staticmethod
    def delete(name):
        try:
            cursor = db.db.conn.cursor()
            cursor.execute("use pdf;")
            cursor.execute("delete from File where name = %s;", [name])
            db.db.conn.commit()
            cursor.close()
        except Exception as e:
            return False
        else:
            return True
    #从数据库中读取文件为bytes
    @staticmethod
    def get_binayry_file_data_from_database(name):
        try:
            cursor = db.db.conn.cursor(dictionary = True)
            cursor.execute("use pdf;")
            cursor.execute("SELECT content from File where name = %s;", [name])
            content = cursor.fetchone()
            db.db.conn.commit()
            cursor.close()
            #print("content", content)
        except Exception as e:
            return b""
        else:
            return content["content"]
    #按照文件名来判断文件是否已经被上传
    @staticmethod
    def check_exists(name):
        try:
            cursor = db.db.conn.cursor(dictionary = True)
            cursor.execute("use pdf;")
            cursor.execute("SELECT * from File where name = %s;", [name])
            r = cursor.fetchall()
            db.db.conn.commit()
            cursor.close()
        except Exception as e:
            return False
        else:
            if r == []:
                return True
            else:
                return False


if __name__ == "__main__":
    print(File.check_exists("my_test.pdf"))