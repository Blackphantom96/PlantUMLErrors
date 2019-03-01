#pip install flask
import io
import os
import time
import datetime
from flask import Flask, jsonify, request, redirect
from settings import *
from main import *

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

    return outfile.getvalue()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
