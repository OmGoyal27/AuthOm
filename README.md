# AuthOm - Flask Password Management System

A secure web-based password management system built with Flask that provides both web interface and JSON API endpoints for password operations.

## Features

- 🔐 **Secure Password Hashing**: Uses SHA-256 for password hashing
- 🌐 **Web Interface**: Beautiful, responsive web interface built with Bootstrap
- 🔄 **Password Change**: Change your password with old password verification
- ✅ **Password Verification**: Verify if your current password is correct
- 🚀 **JSON API**: RESTful API endpoints for programmatic access
- 📱 **Mobile Responsive**: Works seamlessly on desktop and mobile devices
## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment

Copy the example environment file and configure it:

```bash
cp example.env .env
```

Edit `.env` if needed (default configuration should work fine).

### 3. Run the Flask Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Web Interface

### Home Page
- Access the main dashboard at `http://localhost:5000`
- Choose between changing password or verifying password

### Change Password
- Navigate to `http://localhost:5000/change_password`
- Enter your current password
- Set a new password
- Confirm the new password

### Verify Password
- Navigate to `http://localhost:5000/verify_password`
- Enter your password to verify if it's correct

## API Endpoints

### Change Password
```bash
POST /api/change_password
Content-Type: application/json

{
    "old_password": "your_current_password",
    "new_password": "your_new_password"
}
```

**Response:**
```json
{
    "success": true,
    "message": "Password changed successfully"
}
```

### Verify Password
```bash
POST /api/verify_password
Content-Type: application/json

{
    "password": "your_password"
}
```

**Response:**
```json
{
    "success": true,
    "message": "Password verification successful"
}
```

## Command Line Interface

### Run Tests
```bash
python tests.py
```

## File Structure

```
AuthOm/
├── app.py           # Main Flask application
├── main.py               # Core password management functions
├── templates/            # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Home page
│   ├── change_password.html
│   └── verify_password.html
├── data/                 # Data storage
│   └── hashed_passwords.txt
├── tests/                # Test files
├── requirements.txt      # Python dependencies
├── .env                  # Environment configuration
└── README.md
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/OmGoyal27/AuthOm.git
   cd AuthOm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp example.env .env
   ```
   Edit `.env` to set your password file path if needed.

4. **Initialize the password file**
   The system will automatically create the password file with a default empty password hash on first run.

## Usage

### Change Password

Run the main application to change your password:

```bash
python app.py
```

The application will:
1. Prompt for your current password
2. Verify it against the stored hash
3. Prompt for a new password
4. Update the stored password hash

### Core Functions

The [`main.py`](main.py) module provides several key functions:

- **[`hash_password_sha256`](main.py)**: Converts plain text to SHA-256 hash
- **[`get_password_hash_from_user`](main.py)**: Securely prompts user for password and returns hash
- **[`doesPasswordHashMatch`](main.py)**: Verifies if provided hash matches stored password
- **[`update_password_hash`](main.py)**: Updates stored password hash after verification

## Testing

```bash
python tests.py
```

The test suite includes verification of:
- SHA-256 hashing accuracy
- Empty password handling
- Complex password scenarios

## Security Features

- **Password Masking**: Uses `getpass` to hide password input
- **Hash Verification**: Verifies old password before allowing changes
- **Secure Storage**: Only stores SHA-256 hashes, never plain text passwords
- **Default Security**: Creates secure default hash for empty passwords

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `PASSWORD_FILE_PATH` | Path to password hash storage file | `"data/hashed_passwords.txt"` |

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Author

Om Goyal

## Security Features

- **SHA-256 Hashing**: All passwords are hashed using SHA-256 before storage
- **No Plain Text Storage**: Passwords are never stored in plain text
- **Environment Configuration**: Sensitive paths configurable via environment variables
- **Input Validation**: Both client-side and server-side validation
- **Secure Sessions**: Flask sessions for web interface security

## Configuration

Environment variables (set in `.env` file):

- `PASSWORD_FILE_PATH`: Path to the file where hashed passwords are stored (default: `data/hashed_passwords.txt`)

## API Usage Examples

### Using cURL

**Change Password:**
```bash
curl -X POST http://localhost:5000/api/change_password \
  -H "Content-Type: application/json" \
  -d '{"old_password": "oldpass", "new_password": "newpass"}'
```

**Verify Password:**
```bash
curl -X POST http://localhost:5000/api/verify_password \
  -H "Content-Type: application/json" \
  -d '{"password": "yourpassword"}'
```

### Using Python requests

```python
import requests

# Change password
response = requests.post('http://localhost:5000/api/change_password', 
                        json={'old_password': 'oldpass', 'new_password': 'newpass'})
print(response.json())

# Verify password
response = requests.post('http://localhost:5000/api/verify_password', 
                        json={'password': 'yourpassword'})
print(response.json())
```

## Development

### Running in Development Mode

The Flask app runs in debug mode by default when executed directly:

```bash
python flask_app.py
```

### Production Deployment

For production deployment:

1. Set a secure secret key in `flask_app.py`
2. Set `debug=False`
3. Use a production WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 flask_app:app
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## Notes

- The system uses SHA-256 for hashing, which is secure for basic authentication needs
- Password hashes and environment files are excluded from version control
- Default empty password hash: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`