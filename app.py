from flask import Flask, render_template, request, redirect, url_for
import os
import json
from reporter import make_report

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=os.getcwd()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            print ('err: file not in files')
            return redirect('/')

        file = request.files['file']
        if file.filename == '':
            print('err: empty file name')
            return redirect('/')

        if not file.filename.endswith(".json"):
            print('err: invalid file type')
            return redirect('/')

        file.save(file.filename)
        return redirect(url_for('report', filename=file.filename))


@app.route('/report/<filename>')
def report(filename):
    rep = make_report(filename)
    return render_template('report.html', report=rep)

if __name__ == '__main__':
    app.run(debug=True)
