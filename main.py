import hashlib
import getpass
from dotenv import load_dotenv
import os

def get_env_variable(variable_name: str) -> str:
    """
    Retrieves the value of an environment variable.
    If the variable is not set, it raises a KeyError.
    """
    load_dotenv()  # Load environment variables from .env file
    value = os.getenv(variable_name)
    return value

def hash_password_sha256(text: str) -> str:
    """
    Converts the input text into a SHA-256 hashed password (hexadecimal string).
    """
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return sha256_hash

def get_password_hash_from_user(prompt: str = None) -> str:
    """
    Prompts the user to enter a password and returns the hashed version it.
    """
    if not prompt:
        prompt = "Enter your password: "
    password = getpass.getpass(prompt)                     # For now, we are using getpass to get the password
    if not password:
        password = ""
    password_hash = hash_password_sha256(password)
    return password_hash

PASSWORD_FILE_PATH = get_env_variable("PASSWORD_FILE_PATH")
def get_old_password_hash() -> str:
    """
    Reads the old password hash from a file.
    If the file does not exist, it returns an empty string and creates the file.
    """
    try:
        with open(PASSWORD_FILE_PATH, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        with open(PASSWORD_FILE_PATH, "w") as file:
            file.write("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        return "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    
def doesPasswordHashMatch(password_hash: str):
    old_hash = get_old_password_hash()
    if password_hash == old_hash:
        return True
    return False

def update_password_hash(old_pasword: str, new_password_hash: str) -> None:
    """
    Saves the new password hash to a file.

    If there is no old password, just give "" in the place of old_pasword.

    THE GIVEN OLD PASSWORD SHOULD BE IN ITS NORMAL STATE.

    If the old password does not match the new password hash, it does nothing, to not the user know anything.
    """
    
    if not doesPasswordHashMatch(old_pasword):
        return
    
    with open(PASSWORD_FILE_PATH, "w") as file:
        file.write(new_password_hash)

    return "Password hash updated successfully."