#boilerplate basic log-in from stackoverflow
#import json 
import json

#function to prompt user info entry
def login(usr):
    uN = input("Name: ")
    pW = input("Password: ")
    #if user exists & password is correct
    if uN in usr.keys():
        if pW == usr[uN]:
            print("Welcome back.")
        #if user exist but password is wrong
        else:
            print("Incorrect password.")
            return False
    #if user does not exist...write their info as a new user
    else:
        print("Hello, new person.")
        usr[uN] = pW

    writeUsers(usr)
    return True

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w+") as f:
            json.dump(usr, f)
#calls existing user data
users = readUsers()
#input user info
success = login(users)

while not success:
    success = login(users)
