import main
from main import get_password_hash_from_user, doesPasswordHashMatch, update_password_hash, hash_password_sha256

old_password = get_password_hash_from_user("Please enter your old password: ")

if not doesPasswordHashMatch(old_password):
    print("Password did not match the old one.")
    exit()

new_password = get_password_hash_from_user("Enter the new password: ")

if new_password == old_password:
    print("New password cannot be the same as the old password.")
    exit()

output = update_password_hash(old_password, new_password)
print("Returned output: ", output)