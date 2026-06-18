from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    nama = request.form['nama']
    nim = request.form['nim']

    for i in range(1,17):

        file = request.files.get(f'tugas{i}')

        if file and file.filename != '':

            nama_file = f"{nim}_{nama}_tugas{i}.pdf"

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    nama_file
                )
            )

    return '''
    <h2>Tugas berhasil disimpan</h2>
    <a href="/">Kembali</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)