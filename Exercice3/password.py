import hashlib
import getpass


class Password(object):

    def __init__(self, filename):
        self.filename = filename

        while self.ask_action():
            print("\n---------------------------------------------------------------------")

    def ask_action(self):
        print("\n1 - login\n2 - sign in\n3 - leave\n")
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
