import json

class Login:
    def __init__(self):        
        self.users = self.read_users()
        self.codename = None
        self.password = None
        self.last_name = None
        
    def prompt_user(self):
        uStatus = input("Do you have a username? (Y / N)\n")
            if uStatus.upper() == "N":
                uJoin = input("Do you want to become a secret agent? (Y / N)\n")
                if uJoin.upper() == "N":
                    print("Goodbye...you won't remember any of this.\n")
                    return None
                else:
                    return self.new_user()
            elif uStatus.upper() == "Y":
                return self.existing_user()
            else:
                print("Invalid option. Please enter 'Y' or 'N'.\n")

    def new_user(self):
        #add while loop
        uCity = input("Enter a random city: ").replace(" ", "").upper()
        uZip = input("Enter two digits: ")
        uChar = input("Enter two letters: ").upper()
        self.codename = uCity + uZip + uChar
        self.password = input("Password: ").replace(" ", "").upper()

        if self.codename in self.users:
            print("This codename is not available.\n")
            return
            
        self.last_name = input("Enter your last name: ")

        #condense user profile into users.json
        self.users[self.codename] = {
            "last_name": self.last_name,
            "codename": self.codename,
            "password": self.password,
            "bank_balance": "10000",
            "mission_count": "0",
            "fr_shots": "0",
            "fr_hits": "0",
            "fr_score": "0",
            "weapons": {'Glock 17': "1", 'Throwing Knife': "2"},
            "mission_info": {}}
        
        self.write_users()
        print(f"Profile for Agent {self.last_name} initiated successfully...")
        return self.users[self.codename]

    def existing_user(self):
        self.codename = input("Codename: ")
        self.password = input("Password: ")

        if self.codename in self.users:
            if self.password == self.users[self.codename]["password"]:
                #set profile variables to json dictionary for codename
                user_profile = self.users(self.codename)
                #print a confirmation method
                print(f"Welcome back, Agent {user_profile['last_name']}.")
                return user_profile
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

    def write_users(self):
        #replace with your file path so program can locate json
        with open("/custom/path/to/users.json", "w") as f:
            json.dump(self.users, f, indent=4)
