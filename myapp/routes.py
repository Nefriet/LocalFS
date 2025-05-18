from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from myapp import app, db 
import os


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/files', methods=['GET','POST'])
def files():
    upload_dir = app.config['UPLOAD_PATH']
    files = os.listdir(upload_dir)
    return render_template('files_list.html', files=files)

@app.route('/uploads', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            upload_dir = os.path.join(app.config['UPLOAD_PATH']) #Path is in init.py current is 'uploads'
            os.makedirs(upload_dir, exist_ok=True)
            uploaded_file.save(os.path.join(upload_dir, uploaded_file.filename))
        return redirect(url_for('home'))
    return render_template('upload.html')

@app.route('/download/<filename>')
def download(filename):
    directory = 'static/uploads'
    return send_from_directory(directory , filename, as_attachment=True)
    #return f'<h1>{filename}</h1>'