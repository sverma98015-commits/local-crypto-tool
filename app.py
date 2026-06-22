from flask import Flask, render_template, request

from crypto.encryptor import encrypt_text
from crypto.decryptor import decrypt_text
from integrity.hash_verifier import calculate_hash

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    file_hash = ""

    if request.method == "POST":

        action = request.form.get("action")

        if action == "encrypt":

            text = request.form["text"]
            password = request.form["password"]

            result = encrypt_text(text, password)

        elif action == "decrypt":

            text = request.form["text"].strip()
            password = request.form["password"]

            result = decrypt_text(text, password)

        elif action == "hash":

            uploaded_file = request.files["file"]

            if uploaded_file:
                file_hash = calculate_hash(uploaded_file)

    return render_template(
        "index.html",
        result=result,
        file_hash=file_hash
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
