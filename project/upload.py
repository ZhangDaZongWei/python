import os
from flask import Flask, flash, request, send_from_directory, jsonify, render_template,send_from_directory,redirect
from werkzeug.utils import secure_filename
import json
from handleFile.normal import normal 

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','docx','doc'])
pathList = []

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
baseDir = os.path.abspath(os.path.dirname(__file__))

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload_test():
  return render_template('upload.html')

@app.route('/api/upload',methods=['POST'])
def upload_file():
  file_dir = os.path.join(baseDir,app.config['UPLOAD_FOLDER'])
  if not os.path.exists(file_dir):
    os.makedirs(file_dir)
  for f in request.files.getlist("files"):
    if f and allowed_file(f.filename):
      filePath = os.path.join(file_dir,f.filename)
      f.save(filePath)
      pathList.append(filePath)
  with open('uploads.json','w') as write_file:
    json.dump(pathList,write_file)
  return redirect('/show')

@app.route('/show')
def show():
  normal()
  return render_template('render.html')
  
