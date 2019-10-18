import hashlib
import getpass
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class Password(object):

    def __init__(self, filename):
        self.filename = filename
        self.key = None

        while self.ask_action():
            print("\n---------------------------------------------------------------------")

    def ask_action(self):
        print("\n1 - login\n2 - sign in\n3 - encrypt file\n4 - decrypt file\n5 - leave")
        action = input("=> ")

        if action == "1":
            username = input("Enter username : \n=> ")
            password = getpass.getpass("User password : \n=> ")
            self.save(username, password)
        elif action == "2":
            username = input("Enter username : \n=> ")
            password = getpass.getpass("User password : \n=> ")
            self.connect(username, password)
        elif action == "3":
            path = input("path to the file : \n=> ")
            self.key = get_random_bytes(16)
            cipher = AES.new(self.key, AES.MODE_EAX)
            with open(path, mode='rb') as file:  # b is important -> binary
                fileContent = file.read()
                ciphertext, tag = cipher.encrypt_and_digest(fileContent)
            with open("encrypted_"+path, "wb") as file_out:
                [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
        elif action == "4":
            path = input("path to the file : \n=> ")
            with open(path, "rb") as file_in:
                nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
                cipher = AES.new(self.key, AES.MODE_EAX, nonce)
                data = cipher.decrypt_and_verify(ciphertext, tag)
                print(data)
        elif action == "5":
            return False
        return True

    def save(self, username, password):
        with open(self.filename, "w") as fil:
            fil.write(username+"\n"+hashlib.sha512(password.encode()).hexdigest())

    def connect(self, username, password):
        with open(self.filename, "r") as fil:
            if fil.read() == username+"\n"+hashlib.sha512(password.encode()).hexdigest():
                print("BINGO !!!")


Password("logs")
