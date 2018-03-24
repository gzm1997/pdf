import pdf.db as db

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
    
    @staticmethod
    def get_binayry_pdf_data_from_database(name):
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