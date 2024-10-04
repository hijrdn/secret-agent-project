#import json 
import json

#Create Login Class
class Login:
    def __init__(self):
        #need a list of existing users if any; will need to create a function for this later
        self.users = self.read_users()
        self.codename = None
        self.password = None
        self.last_name = None
        
    def prompt_user(self):
        uStatus = input("Do you have a username? (Y / N)\n")
            uJoin = input("Do you want to become a secret agent? (Y / N)\n")
            if uJoin == "N":
                print("Goodbye...you won't remember any of this.\n")
                return
            else:
                self.new_user()
        else:
            self.existing_user()

    def new_user(self):
        uCity = input("Enter a random city: ").replace(" ", "").upper()
        uZip = input("Enter two digits: ")
        uChar = input("Enter two letters: ").upper()
        self.codename = uCity + uZip + uChar
        self.password = input("Password: ").replace(" ", "").upper()

        if self.codename in self.users:
            print("This codename is not available.\n")
            return
            
        self.last_name = input("Enter your last name: ")

        bank_balance = "10000"
        mission_count = "0"
        fr_shots = "0"
        fr_hits = "0"
        fr_score = "o"
        weapons = ["Glock 17", "Throwing Knife"]

        user_profile = {
            "last_name": self.last_name,
            "codename": self.codename,
            "password": self.password,
            "bank_balance": bank_balance,
            "mission_count": mission_count,
            "fr_shots": fr_shots,
            "fr_hits": fr_hits,
            "fr_score": fr_score,
            "weapons": weapons,}

        #function for creating a save-file for the user; needs to be written
        self.save_profile(self.codename, user_profile)
        #function for associating codename and password with each other in the users dictionary
        self.users[self.codename] = self.password
        #function for writing updated users dictionary to json
        self.write_users()
        #notification for user that profile is created; also for error catching
        print(f"Profile for Agent {self.last_name} initiated successfully...")

    def existing_user(self):
        self.codename = input("Codename: ")
        self.password = input("Password: ")

        if self.codename in self.users:
            if self.password == self.users[self.codename]:
                #set profile variables to json dictionary for codename
                #needs a load_profile function
                user_profile = self.load_profile(self.codename)
                #load last_name from dictionary
                self.last_name = user_profile.get("last_name")
                #print a confirmation method
                print(f"Welcome back, Agent {self.last_name}.")
            else:
                print("Incorrect password...")
        else:
            print("Codename not found. Please try again or register with a recruiter.")
            
    def read_users(self):
        #replace with your file path so program can locate users.json
        try:
            with open("/custom/path/to/users.json", "r") as f:
                return json.load(f)
        #if no file, return empty dict
        except FileNotFoundError:
            return {}
