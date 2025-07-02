# AuthOm

A simple password authentication system that uses SHA-256 hashing to securely store and verify passwords.

## Features

- **Secure Password Hashing**: Uses SHA-256 algorithm to hash passwords
- **Password Change Functionality**: Allows users to securely change their passwords
- **Environment Configuration**: Uses environment variables for configuration
- **File-based Storage**: Stores hashed passwords in a local file
- **Comprehensive Testing**: Includes unit tests for password hashing functionality

## Project Structure

```
AuthOm/
├── app.py                 # Main application for password change workflow
├── main.py               # Core authentication functions
├── tests.py              # Test runner script
├── .env                  # Environment variables (not tracked)
├── example.env           # Example environment configuration
├── data/
│   └── hashed_passwords.txt  # Stored password hashes (not tracked)
└── tests/
    └── test_main.py      # Unit tests for authentication functions
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