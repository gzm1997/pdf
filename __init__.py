# _*_ coding: utf-8 _*_
from flask import Flask
from flask import render_template
from flask import make_response
from flask.views import MethodView
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import random, string
import os
import pdf.db
import pdf.f

#设置允许上传的文件类型为pdf
ALLOWED_EXTENSIONS = set(['pdf'])
#声明一个flask应用
app = Flask(__name__)
#判断文件名是否合法
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#第一次请求之前初始化数据库
@app.before_first_request
def init_db():
    db.init_db()
#上传文件的视图对象
class Upload_file(MethodView):
    #get方法的视图函数
    def get(self):
        return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
                <p>
                    <input type=file name=file>
                    <input type=submit value=Upload>
                </p>
            </form>
        '''
    #post方法的视图函数
    def post(self):
        file = request.files["file"]
        filename = secure_filename(file.filename)
        content = file.stream.read()
        #如果文件大小超过16m
        if len(content) > 16 * pow(2, 20):
            return "the file is too big to upload, the Maximum length of file is 16m bytes"
        #如果可以上传
        if file and allowed_file(file.filename) and f.File.check_exists(filename):
            #print("lala")
            pdf_file = f.File(filename, content)
            if pdf_file.save():
                return redirect(url_for("show", file_name = filename))
            else:
                return "upload failed!"
        #如果从文件名中得知已经上传了
        elif file and allowed_file(file.filename) and not f.File.check_exists(filename):
            print("heihei")
            return redirect(url_for("show", file_name = filename))
        else:
            return "the file is empty or filename is not allowed"
#将视图对象转为视图函数
app.add_url_rule("/upload", view_func = Upload_file.as_view("upload"))
#展示上传的pdf文件
@app.route("/show")
def show():
    file_name = request.args.get("file_name")
    pdf = f.File.get_binayry_pdf_data_from_database(file_name)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % file_name
    return response
    

if __name__ == "__main__":
    app.run(debug = True)