import hashlib

def hash_password_sha256(text: str) -> str:
    """
    Converts the input text into a SHA-256 hashed password (hexadecimal string).
    """
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return sha256_hash

print(hash_password_sha256("password"))  # Example usage