from flask import Flask, render_template
from flask import request, redirect, url_for, abort
import os, sys

app = Flask(__name__)

# Setting global variables
app.config['UPLOAD_FOLDER'] = 'static/files/upload_data/'
if not os.path.isdir(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def hello_flask():
   return 'Hello Flask!'

@app.route('/hello/<name>', methods=['POST', 'GET'])
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
