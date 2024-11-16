from getpass import getpass
from cryptography.fernet import Fernet
import json

# Generate a key for encryption and decryption
# Store this key securely. If lost, regenerate it and store new encrypted password
key = Fernet.generate_key()
print(f"Encryption key: {key.decode()}")  # Print this key and store it securely

# Create a cipher object using the key
cipher = Fernet(key)

# Define the password to be encrypted
password = getpass()

# Encrypt the password
encrypted_password = cipher.encrypt(password.encode())

# Write the encrypted password to credentials.json
with open('credentials.json', 'r') as f:
    data = json.load(f)
data['password'] = encrypted_password

with open('credentials.json', 'w') as f:
    json.dump(data, f)

print('Password encrypted and saved to credentials.json')
