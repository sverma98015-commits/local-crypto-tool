import hashlib

def calculate_hash(file):

    sha256 = hashlib.sha256()

    while True:
        chunk = file.read(4096)

        if not chunk:
            break

        sha256.update(chunk)

    file.seek(0)

    return sha256.hexdigest()
