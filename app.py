from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def index():

    pesan = ""

    if request.method == "POST":

        nama = request.form["nama"]
        nim = request.form["nim"]

        folder_mahasiswa = os.path.join(
            app.config["UPLOAD_FOLDER"],
            nim
        )

        if not os.path.exists(folder_mahasiswa):
            os.makedirs(folder_mahasiswa)

        for i in range(1, 7):

            file = request.files.get(f"tugas{i}")

            if file and file.filename != "":

                nama_file = secure_filename(
                    f"Tugas_{i}_{nama}_{nim}.pdf"
                )

                file.save(
                    os.path.join(
                        folder_mahasiswa,
                        nama_file
                    )
                )

        pesan = "Tugas berhasil dikumpulkan!"

    return render_template(
        "index.html",
        pesan=pesan
    )


if __name__ == "__main__":
    app.run(debug=True)