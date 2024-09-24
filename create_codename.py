# Creates a secret codename for the user
# Organize text options in a dictionary for simpler code organization

intro_text = {'Q1': 'Do you want to become a secret agent? (Y / N)\n',
              'Y': 'Welcome to the agency. Lets setup your codename.',
              'city': 'Pick a random city: ',
              'zipcode': 'Pick two digits from your current zipcode: ',
              'dishware': 'Pick a utensil or dishware: ',
              'N': 'Understandable. You wont remember this. But I will....',
              'initialize': 'Initializing agent profile.',
              'dots': '.....',
              'hello': 'Hello, Agent.',}
menu_text = {'gen': 'What do you need? (money / weapons / firing range)\n',
             'money': 'Your bank account balance is $5,000,020.40.',
             'weapons': 'You have two custom 9mm pistols, an M14, and three throwing knives. As well as some surpressors.',
             'firing range': 'Welcome to the firing range.',
             'next': 'What would you like to do next?',
             'loop': '(menu / leave)\n',
             'leave': 'Best of luck out there, Agent.',}

# Opportunity for the user to opt out
start = input(intro_text['Q1'])
# Code for answer Y
if start == "Y":
    # Prints text to welcome the user
    print(intro_text['Y'])

    # 3 questions for the user
    city = input(intro_text['city'])
    zipcode = input(intro_text['zipcode'])
    dishware = input(intro_text['dishware'])

    agent_name = dishware + zipcode + city

    # Creates the codename for the user
    print(intro_text['initialize'])
    print(intro_text['dots'])
    print(intro_text['hello'])
    print(agent_name)

    # Prompt agent with a menu
    print(menu_text['next'])
    selection = input(menu_text['loop'])

    while selection == "menu":
        menu = input(menu_text['gen'])
        if menu == "money":
            print(menu_text['money'])
        elif menu == "weapons":
            print(menu_text['weapons'])
        elif menu == "firing range":
            print(menu_text['firing range'])
        else:
            print(menu_text['next'])
            selection = input(menu_text['loop'])
    print(menu_text['leave'])

else:
    print(intro_text['N'])
