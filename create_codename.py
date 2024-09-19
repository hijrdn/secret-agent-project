# Creates a secret codename for the user
# Opportunity for the user to opt out
start = input("Do you want to become a secret agent? Y / N ")

# Code for answer Y
if start == "Y":

    # Prints text to welcome the user
    print("Welcome to the agency. Let's setup your codename.")

    # 3 questions for the user
    city = input("Pick a random city: ")
    zipcode = input("Pick two digits from your current zipcode: ")
    dishware = input("Pick a utensil or dishware: ")

    agent_name = dishware + zipcode + city

    # Creates the codename for the user
    print("Initializing agent profile.")
    print(".....")
    print(f"Hello, Agent {agent_name}.")

    # Prompt agent with a menu
    print("What would you like to do next?")
    selection = input("Menu / Leave ")

    while selection == "Menu":
        menu = input("Things move quickly. What do you need? Money or weapons? ")
        if menu == "money":
            print("Your bank account balance is $5,000,020.40.")
        elif menu == "weapons":
            print("You have two custom 9mm pistols, an M14, and three throwing knives. As well as some surpressors.")
        else:
            print("What would you like to do next? ")
            selection = input("Menu / Leave ")
    print(f"Best of luck out there, Agent {agent_name}.")
        
# Code for answer N
else:
    print("Understandable. You won't remember this. But I will....")
