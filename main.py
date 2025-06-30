import hashlib
import getpass

def hash_password_sha256(text: str) -> str:
    """
    Converts the input text into a SHA-256 hashed password (hexadecimal string).
    """
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return sha256_hash

def get_password_hash_from_user() -> str:
    """
    Prompts the user to enter a password and returns it.
    """
    password = getpass.getpass("Enter your password: ")                     # For now, we are using getpass to get the password
    password_confirmation = getpass.getpass("Confirm your password: ")      # Later we will use a GUI input method
    if password != password_confirmation:
        raise ValueError("Passwords do not match.")
    
    password_hash = hash_password_sha256(password)
    return password_hash