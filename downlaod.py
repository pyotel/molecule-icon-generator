from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is a simple file download service!'

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join('./', filename)
    print(file_path)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'File not found!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
