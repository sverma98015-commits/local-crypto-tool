from flask import Flask, render_template, request
from crypto.encryptor import encrypt_text
from crypto.decryptor import decrypt_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        text = request.form["text"]
        password = request.form["password"]

        if request.form["action"] == "encrypt":
            result = encrypt_text(text, password)

        elif request.form["action"] == "decrypt":
            result = decrypt_text(text, password)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
