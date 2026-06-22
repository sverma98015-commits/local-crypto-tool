# Local Cryptographic Text Encryptor & Hash Verifier

A security-focused desktop application developed in Python for secure text protection, cryptographic integrity verification, and local file authentication. The application leverages industry-standard cryptographic primitives from the Python Cryptography ecosystem to provide robust encryption, decryption, and hash-based verification capabilities while adhering to modern security best practices.

![Full Application Layout](screenshots/FULL.JPG)

---

##  Key Features

### AES-256 Secure Encryption & Decryption

* Implements AES-256 symmetric encryption in CBC mode for strong confidentiality.
* Uses cryptographically secure random Initialization Vectors (IVs) generated for every encryption operation.
* Derives encryption keys from user-supplied passphrases using secure password-based key derivation techniques.
* Supports secure encryption and decryption of sensitive textual data.
* Prevents key reuse and eliminates hardcoded cryptographic secrets.
* ![Encryption Module](screenshots/A.jpg)
  ![Decryption Module](screenshots/B.jpg)

###  Secure Key Derivation & Salting

* Integrates randomly generated salts to strengthen password-derived keys.
* Protects against rainbow table and precomputed dictionary attacks.
* Ensures unique cryptographic outputs even when identical passwords are used.

###  SHA-256 Hash Generation

* Computes deterministic SHA-256 cryptographic hashes for local files.
* Generates unique digital fingerprints for integrity validation.
* Enables quick verification of downloaded files, backups, and critical documents.

* ![Hash Generator](screenshots/C.JPG)

### File Integrity Verification

* Compares computed SHA-256 hashes against trusted reference values.
* Detects unauthorized file modification, corruption, or tampering.
* Provides clear verification results for security auditing and file validation workflows.
* ![Integrity Verification](screenshots/F.JPG)

###  Modern Glassmorphic User Interface

* Clean and responsive desktop interface.
* Glassmorphism-inspired design with translucent panels and blur effects.
* User-friendly workflow for encryption, decryption, hashing, and verification operations.
* Designed for both educational cryptography demonstrations and practical local security usage.

---

## Technical Architecture

### Cryptographic Components

| Component            | Technology                             |
| -------------------- | -------------------------------------- |
| Encryption Algorithm | AES-256                                |
| Cipher Mode          | CBC (Cipher Block Chaining)            |
| Hashing Algorithm    | SHA-256                                |
| Key Generation       | Password-Based Key Derivation          |
| Salt Generation      | Cryptographically Secure Random Values |
| IV Generation        | Secure Random Initialization Vectors   |

### Security Practices Implemented

* No hardcoded encryption keys.
* Secure random number generation.
* Unique IV for every encryption operation.
* Salted password-derived keys.
* Proper separation of encryption and integrity verification logic.
* Safe handling of sensitive cryptographic materials.

---

## Technology Stack

* Python
* Cryptography Library
* Hashlib
* Tkinter / Custom GUI Framework
* Secure Random Generators (os.urandom)

---

## Security Considerations

The application follows fundamental cryptographic best practices by:

* Avoiding weak random number generators.
* Preventing static key reuse.
* Using industry-standard encryption and hashing algorithms.
* Maintaining confidentiality through AES-256 encryption.
* Ensuring integrity verification through SHA-256 checksums.

---

## Use Cases

* Secure storage of confidential notes.
* Password-protected message encryption.
* File authenticity verification.
* Malware-free software download verification.
* Digital forensic and cybersecurity learning environments.
* Educational demonstrations of modern cryptographic principles.

---

## Learning Outcomes

Through this project, practical experience was gained in:

* Applied Cryptography
* Symmetric Encryption
* Secure Key Management
* Hash Functions and Integrity Checking
* Secure Software Development Practices
* Cybersecurity Tool Development
* Python Security Programming
