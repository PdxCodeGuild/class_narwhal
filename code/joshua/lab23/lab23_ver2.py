'''
Josh Novac
Lab 23
Version_2
Python
PDX Code Guild
'''


'''////////////////////////VERSION_1////////////////////////'''

with open("contacts.csv") as file:
        lines = file.read().split('\n')

contacts = []

for line in range(1, len(lines)):
    keys = lines[0]
    values = lines[line]
    keys = keys.split(',')
    values = values.split(',')
    contact_dict = dict(zip(keys, values))
    contacts.append(contact_dict)

# print(contacts)

'''////////////////////////VERSION_2////////////////////////'''

def Create():
    new_name = input(f'Enter name of contact: ').title()
    create_new = dict(zip(keys, new_name))
    choice_menu()

def Retrieve():
    print('Your current contacts: ')
    for x in contacts:
        print(x['name'])
    get_contact = input('Who do you want to look up? \n>').title()
    for x in contacts:
        if get_contact == x['name']:
            print(x)
    choice_menu()

    

def Update():
    for x in contacts:
        print(x['name'])
    record = grab_info()

    update_info = input('What information do you want to update?\nName, Color, or Fruit?\t(or type \'quit\' to quit) ')
    if update_info == 'name':
        new_name = input('Change name to: ').title()
        print(f'Contact name was changed to {new_name}!')
        choice_menu()
    elif update_info == 'color':
        new_color = input('Change color to: ').title()
        print(f'Your contact\'s color was changed to {new_color}!')
        choice_menu()
    elif update_info == 'fruit':
        new_fruit = input('Change fruit to: ').title()
        print(f'Your contact\'s fruit was changed to {new_fruit}!')
        choice_menu()
    elif update_info == 'quit':
        choice_menu()

def Delete():
    for x in contacts:
        print(x['name'])
    record = grab_info_delete()
    ask_remove = input('Are you sure? \'Yes\' or \'No\'?\n>').lower()
    if ask_remove == 'yes':
        print('Contact deleted! ')
        choice_menu()
    elif ask_remove == 'no':
        choice_menu()

def grab_info():
    profile = input('Which user do you want to update? \n>').lower()
    for record in contacts:
        if record['name'] == profile:
            return record

def grab_info_delete():
    profile = input('Which user do you want to delete? \n>').lower()
    for record in contacts:
        if record['name'] == profile:
            return record

## main menu function
def choice_menu():
    user_choice = input('\n////MAIN MENU////\n\nWhat do you want to do?\n\nC - Create?\nR - Retrieve?\nU - Update?\nD - Delete?\n>').lower()
    if user_choice == 'c':
        Create()
    elif user_choice == 'r':
        Retrieve()
    elif user_choice == 'u':
        Update()
    elif user_choice == 'd':
        Delete()