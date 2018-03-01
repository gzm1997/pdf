# _*_ coding: utf-8 _*_

from flask import Flask
from flask import render_template
import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import random, string


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            length = 16
            folder_name = ''.join([random.choice(string.ascii_letters) for i in range(length)])
            os.makedirs("./static/" + folder_name)
            file.save(os.path.join("./static/" + folder_name, filename))
            return redirect(url_for("show", folder_name = folder_name, file_name = filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

#/show?folder_name=a&file_name=b
@app.route("/show")
def show():
	folder_name = request.args.get("folder_name")
	file_name = request.args.get("file_name")
	return render_template("show.html", pdf_url = "./static/" + folder_name + "/" + file_name)

if __name__ == "__main__":
	app.run(debug = True)