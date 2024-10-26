from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def generate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

def generate_sha1(input_string):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_string.encode('utf-8'))
    return sha1_hash.hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    md5_result = ''
    sha1_result = ''
    input_string = ''

    if request.method == 'POST':
        input_string = request.form['input_string']
        md5_result = generate_md5(input_string)
        sha1_result = generate_sha1(input_string)

    return render_template('index.html', md5=md5_result, sha1=sha1_result, input_string=input_string)

if __name__ == '__main__':
    app.run(debug=True)
