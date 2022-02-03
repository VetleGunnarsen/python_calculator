from cryptography.fernet import Fernet

masterpwd = input("Enter master password: ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key,", "wb") as key_file:
        key_file.write(key)


def view():
    with open('passwrods.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "Password: ", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwrods.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would u like to add a new password or view a new one (view, add)?, press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
            view()
    elif mode == "add":
            add()
    else:
        print("invalid mode")
        continue
    
