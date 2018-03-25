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


ALLOWED_EXTENSIONS = set(['pdf'])
app = Flask(__name__)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.before_first_request
def init_db():
    db.init_db()

class Upload_file(MethodView):    
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

    def post(self):
        file = request.files["file"]
        filename = secure_filename(file.filename)
        content = file.stream.read()
        if len(content) > 16 * pow(2, 20):
            return "the file is too big to upload, the Maximum length of file is 16m bytes"
        if file and allowed_file(file.filename) and f.File.check_exists(filename):
            print("lala")
            pdf_file = f.File(filename, content)
            if pdf_file.save():
                return redirect(url_for("show", file_name = filename))
            else:
                return "upload failed!"
        elif file and allowed_file(file.filename) and not f.File.check_exists(filename):
            print("heihei")
            return redirect(url_for("show", file_name = filename))
        else:
            return "the file is empty or filename is not allowed"
        


app.add_url_rule("/upload", view_func = Upload_file.as_view("upload"))

#/show?file_name=b
@app.route("/show")
def show():
    file_name = request.args.get("file_name")
    pdf = f.File.get_binayry_pdf_data_from_database(file_name)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % 'yourfilename'
    return response
    

if __name__ == "__main__":
    app.run(debug = True)