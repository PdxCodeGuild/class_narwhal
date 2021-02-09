# ---- Lab 23 ---- #

# - Contact List - #

# - Version 1 - #
# - Format the CSV file - #

contact_list = []

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    header = lines[0].split(',') # turn the first line into headers
    for i in range(1, len(lines)): # skip the headers
        row = lines[i].split(',')  # give the rows value
        contact = dict(zip(header, row)) # zip 'em up into a dicitonary
        contact_list.append(contact) # toss it into the contact_list list

# - Version 2 - #
# - Create, Read, Update and Delete Functions - #

def create(contact_list, header):
    new = {}
    for key in header:
        new[key] = input(f"What is your new contacts '{key}'? ")
    contact_list.append(new)

def cont_read(contact_list):
    read = input('Please enter the name of the contact? ')
    for contact in contact_list:
        c = contact
        if c.get("name") == read:
             print(f'''
             {c}''')

# Separate READ function for the UPDATE and DELETE functions
def read(contact_list):
    read = input('Please enter the name of the contact? ')
    for contact in contact_list:
        c = contact
        if c.get("name") == read:
            return c

def update(contact_list):
    contact = read(contact_list)
    category_to_update = input("Please enter the category you would like to update: ")
    new_value = input(f"What would you like to change it to?  ")
    contact[category_to_update] = new_value
    return contact

def delete(contact_list):
    delete = read(contact_list)
    for i, contact in enumerate(contact_list):
        if contact == delete:
            del contact_list[i]

# - Implement a CRUD REPL - #

while True:
    print('''
    Welcome to your Contacts List!''')
    while True:
        print("""
        Enter 'Done' if you are finished.""")
        task = input("Would you like to 'Create', 'Read', 'Update', or 'Delete' a contact? ").lower()
        if task == 'done':
            print('''
            Have a good day!''')
            break
        elif task == 'create':
            create(contact_list, header)
        elif task == 'read':
            cont_read(contact_list)
        elif task == 'update':
            update(contact_list)
        elif task == 'delete':
            delete(contact_list)

# - Version 3 - #
# - Save the updated Contact List CSV - #

    topline = [','.join(header)]
    for contact in contact_list:
        rows = ','.join(contact.values()) # turn the contacts into strings separated by commas
        topline.append(rows) # add to the lines list of headers
    new_list = '\n'.join(topline) # turn lines into a string
    with open('contacts.csv', 'w') as file:
        file.write(new_list) # write over the contacts.csv file
    break