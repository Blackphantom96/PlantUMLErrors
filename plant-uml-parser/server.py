#pip install flask
import io
import os
import time
import datetime
from flask import Flask, jsonify, request, redirect
from settings import *
from prologParser import *
from main import *
from pyswip import Prolog


# You can change this to any folder on your system
app = Flask(__name__)

def get_timestamp() -> str:
    now = datetime.datetime.now()
    return "{}/{}/{} {}:{}:{}".format(now.year,
                                      now.month,
                                      now.day,
                                      now.hour,
                                      now.minute,
                                      now.second)

def process_prolog_files(assertz_fs, queries_fs):
    """Load the uploaded file"""
    assertz_bytes = io.BytesIO()
    queries_bytes = io.BytesIO()
    assertz_fs.save(assertz_bytes)
    queries_fs.save(queries_bytes)

    assertz_byte_str = assertz_bytes.getvalue()
    queries_byte_str = queries_bytes.getvalue()

    assertz_text_obj = assertz_byte_str.decode('UTF-8')
    queries_text_obj = queries_byte_str.decode('UTF-8')
    
    assertz_infile = io.StringIO(assertz_text_obj)
    queries_infile = io.StringIO(queries_text_obj)
    outfile = io.StringIO()

    print(assertz_infile)
    print(queries_infile)
    
    start_prolog(assertz_infile, queries_infile, outfile)

    print("Llega")

    return outfile.getvalue()

@app.route('/prolog', methods=['GET', 'POST'])
def process_prolog():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        assertz = request.files['assertz']
        queries = request.files['queries']
        
        return process_prolog_files(assertz, queries)

    return '''
    <!doctype html>
    <h1>Upload a file</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="assertz">
      <input type="file" name="queries">
      <input type="submit" value="Upload">
    </form>
    '''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        file = request.files['file']
        
        return process_file(file)

    return '''
    <!doctype html>
    <h1>Upload a file</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


def process_file(file_stream):
    """Load the uploaded file"""
    infile_bytes = io.BytesIO()
    outfile = io.StringIO()
    file_stream.save(infile_bytes)

    byte_str = infile_bytes.getvalue()

    text_obj = byte_str.decode('UTF-8')
    infile = io.StringIO(text_obj)
    
    start(infile, outfile)
    f = open("assert.pl","w")
    f.write(outfile.getvalue())
    f.close()
    res = query()
    
    return outfile.getvalue()

def query():
  """Make a prolog Query"""
  res = []
  prolog = Prolog()
  try:
    # prolog.consult("project.pl")
    pass
  except expression as identifier:
    pass
  # res.append(queryResult(prolog.query('multiplicityError(X)')))
  # res.append(queryResult(prolog.query('warningAlone(X)')))
  return res

def queryResult(query):
  try:
    return list(query)
  except expression as identifier:
    return ""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
