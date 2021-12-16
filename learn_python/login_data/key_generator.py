from cryptography.fernet import Fernet

def write_key():        # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():         #Load the key from key.key file
    return open("key.key", "rb").read()

write_key()
key = load_key()
f = Fernet(key)
file = "login_data.txt"

def deleteContent(file):
    file.seek(0)
    file.truncate()

username = "username".encode()
line = "\n".encode()
password = "password".encode()

encrypted_u = f.encrypt(username)
encrypted_p = f.encrypt(password)

with open("login_data.txt", "r+b") as f:
    f.write(encrypted_u)
    f.write(line)
    f.write(encrypted_p)
