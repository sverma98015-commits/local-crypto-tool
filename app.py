from flask import Flask, render_template, request

from crypto.encryptor import encrypt_text
from crypto.decryptor import decrypt_text
from integrity.hash_verifier import calculate_hash

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    file_hash = ""
    verification_result = ""

    if request.method == "POST":

        action = request.form.get("action")

        try:

            if action == "encrypt":

                text = request.form["text"]
                password = request.form["password"]

                result = encrypt_text(text, password)

            elif action == "decrypt":

                text = request.form["text"].strip()
                password = request.form["password"]

                result = decrypt_text(text, password)

            elif action == "hash":

                uploaded_file = request.files.get("file")

                if uploaded_file and uploaded_file.filename:

                    file_hash = calculate_hash(uploaded_file)

                else:

                    file_hash = "Please select a file."

            elif action == "verify":

                uploaded_file = request.files.get("verify_file")
                expected_hash = request.form.get(
                    "expected_hash",
                    ""
                ).strip()

                if not uploaded_file or not uploaded_file.filename:

                    verification_result = (
                        "Please select a file."
                    )

                elif not expected_hash:

                    verification_result = (
                        "Please enter an expected hash."
                    )

                else:

                    generated_hash = calculate_hash(
                        uploaded_file
                    )

                    if generated_hash.lower() == expected_hash.lower():

                        verification_result = (
                            "✓ Integrity Verified"
                        )

                    else:

                        verification_result = (
                            "✗ Hash Mismatch - File Modified"
                        )

        except Exception as e:

            result = f"Error: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        file_hash=file_hash,
        verification_result=verification_result
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
