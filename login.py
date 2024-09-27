#import json 
import json

#Create Login Class
class Login:
    #function to initialize class attributes
    def __init__(self):
        #need a list of existing users if any; will need to create a function for this later
        self.users = self.read_users()
        #need to empty values related to user prompts
        self.codename = None
        self.password = None
        self.last_name = None
        
    #function to prompt user to select a login method
    def prompt_user(self):
        uStatus = input("Do you have a username? (Y / N)\n")
            uJoin = input("Do you want to become a secret agent? (Y / N)\n")
            if uJoin == "N":
                print("Goodbye...you won't remember any of this.\n")
                return
            else:
                self.new_user()
        #will need to create a function for this later
        else:
            self.existing_user()

    #if user indicates they are new, function to create profile
    def new_user(self):
        uCity = input("Enter a random city: ").replace(" ", "").upper()
        uZip = input("Enter two digits: ")
        uChar = input("Enter two letters: ").upper()
        self.codename = uCity + uZip + uChar
        self.password = input("Password: ").replace(" ", "").upper()

        #if codename entered is taken; exit; needs read_user function created later
        if self.codename in self.users:
            print("This codename is not available.\n")
            return
            
        #next prompt so user can be referred to by last name
        self.last_name = input("Enter your last name: ")
