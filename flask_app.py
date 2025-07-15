from flask import Flask, render_template, request, flash, redirect, url_for, session
import hashlib
import os
from dotenv import load_dotenv
from main import hash_password_sha256, get_old_password_hash, doesPasswordHashMatch, update_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this in production

# Load environment variables
load_dotenv()

@app.route('/')
def index():
    """Home page with options to change password or verify password"""
    return render_template('index.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    """Route to change password"""
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if not old_password or not new_password or not confirm_password:
            flash('All fields are required.', 'error')
            return render_template('change_password.html')
        
        if new_password != confirm_password:
            flash('New password and confirmation do not match.', 'error')
            return render_template('change_password.html')
        
        # Hash the old password and check if it matches
        old_password_hash = hash_password_sha256(old_password)
        if not doesPasswordHashMatch(old_password_hash):
            flash('Old password is incorrect.', 'error')
            return render_template('change_password.html')
        
        # Hash the new password
        new_password_hash = hash_password_sha256(new_password)
        
        if new_password_hash == old_password_hash:
            flash('New password cannot be the same as the old password.', 'error')
            return render_template('change_password.html')
        
        # Update the password
        result = update_password_hash(old_password_hash, new_password_hash)
        if result:
            flash('Password changed successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Failed to update password. Please try again.', 'error')
    
    return render_template('change_password.html')

@app.route('/verify_password', methods=['GET', 'POST'])
def verify_password():
    """Route to verify current password"""
    if request.method == 'POST':
        password = request.form.get('password')
        
        if not password:
            flash('Password is required.', 'error')
            return render_template('verify_password.html')
        
        password_hash = hash_password_sha256(password)
        if doesPasswordHashMatch(password_hash):
            flash('Password verification successful!', 'success')
        else:
            flash('Password verification failed.', 'error')
    
    return render_template('verify_password.html')

@app.route('/api/change_password', methods=['POST'])
def api_change_password():
    """API endpoint for changing password (JSON)"""
    data = request.get_json()
    
    if not data:
        return {'success': False, 'message': 'No data provided'}, 400
    
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    
    if not old_password or not new_password:
        return {'success': False, 'message': 'Both old and new passwords are required'}, 400
    
    old_password_hash = hash_password_sha256(old_password)
    if not doesPasswordHashMatch(old_password_hash):
        return {'success': False, 'message': 'Old password is incorrect'}, 401
    
    new_password_hash = hash_password_sha256(new_password)
    if new_password_hash == old_password_hash:
        return {'success': False, 'message': 'New password cannot be the same as the old password'}, 400
    
    result = update_password_hash(old_password_hash, new_password_hash)
    if result:
        return {'success': True, 'message': 'Password changed successfully'}
    else:
        return {'success': False, 'message': 'Failed to update password'}, 500

@app.route('/api/verify_password', methods=['POST'])
def api_verify_password():
    """API endpoint for verifying password (JSON)"""
    data = request.get_json()
    
    if not data:
        return {'success': False, 'message': 'No data provided'}, 400
    
    password = data.get('password')
    if not password:
        return {'success': False, 'message': 'Password is required'}, 400
    
    password_hash = hash_password_sha256(password)
    if doesPasswordHashMatch(password_hash):
        return {'success': True, 'message': 'Password verification successful'}
    else:
        return {'success': False, 'message': 'Password verification failed'}, 401

if __name__ == '__main__':
    # Ensure the data directory exists
    password_file_path = os.getenv('PASSWORD_FILE_PATH', 'data/hashed_passwords.txt')
    os.makedirs(os.path.dirname(password_file_path), exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
