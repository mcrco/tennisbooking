from cryptography.fernet import Fernet
import json

# Generate a key for encryption and decryption
# You must store this key securely. If you lose it, you will not be able to decrypt the data.
key = Fernet.generate_key()
print(f"Encryption key: {key.decode()}")  # Print this key and store it securely

# Create a cipher object using the key
cipher = Fernet(key)

# Define the password to be encrypted
password = ''

# Encrypt the password
encrypted_password = cipher.encrypt(password.encode())

# Write the encrypted password to credentials.json
with open('credentials.json', 'r') as f:
    data = json.load(f)
data['password'] = encrypted_password

with open('credentials.json', 'w') as f:
    json.dump(data, f)

print('Password encrypted and saved to credentials.json')
