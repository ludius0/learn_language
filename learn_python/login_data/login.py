from cryptography.fernet import Fernet
from getpass import getpass

l_list = []

def load_key():
    return open("key.key", "rb").read()


def get_data(file):
    global l_list
    with open(file, "r") as fl:
        for item in fl:
            l_list.append(item)

    l_list = [i.split('\n', 1)[0] for i in l_list]
    

def encrypt(file, key, username, password):
    f = Fernet(key)

    username = input("Write new username: ").encode()
    password = getpass("Write new password: ").encode()
    
    open('login_data.txt', 'w').close()
    
    encrypted_username = f.encrypt(username)
    line = "\n".encode()
    encrypted_password = f.encrypt(password)

    with open(file, "w+b") as fl:
        fl.write(encrypted_username)
        fl.write(line)
        fl.write(encrypted_password)


def decrypt(key, username, password):
    f = Fernet(key)
    global decrypted_username
    global decrypted_password
    
    username = username.encode()
    password = password.encode()
    
    decrypted_username = f.decrypt(username)
    decrypted_password = f.decrypt(password)

    decrypted_username = decrypted_username.decode()
    decrypted_password = decrypted_password.decode()


        
key = load_key()
file = "login_data.txt"

get_data(file)


def main():
    while True:
        f = Fernet(key)
        get_data(file)
        
        user_username = input("Input username: ")
        user_password = getpass("Input password: ")

        username = l_list[0]
        password = l_list[1]

        decrypt(key, username, password)

        if user_username == decrypted_username and user_password == decrypted_password:
            user_choice = input("Congratulation -> You are in.\nNow change username and password:\n")

            encrypt(file, key, username, password)
                
            print("Program will now close.\nReopen it again.")
            break
          
        else:
            print("Nope! Try again!")

main()
    
print("Goodbye")
