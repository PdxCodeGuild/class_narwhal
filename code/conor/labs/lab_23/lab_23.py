# ---- Lab 23 ---- #

# - Contact List - #

# - Version 1 - #
# - Format the CSV file - #

contact_list = []

with open('contacts.csv') as file:
    lines = file.read().split('\n')
    header = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(header, row))
        contact_list.append(contact)


print(contact_list)

# - Version 2 - #
# - Create, Read, Update and Delete Functions - #

def create(contact_list, header):
    new = {}
    for key in header:
        new[key] = input(f"What is your new contacts '{key}'? ")
    contact_list.append(new)

# create(contact_list, header)
# print(contact_list)

def read(contact_list):
    read = input('What is the name of the contact you would like to see? ')
    for contact in contact_list:
        c = contact
        if c.get("name") == read:
            return c

# print(read(contact_list, header))

def update(contact_list):
    update = read(contact_list)
    contact_to_update = input("Please enter the category you would like to update: ")
    update_contact = input(f"What would you like to change it to?  ")
    update[contact_to_update] = update_contact
    return update

# print(update(contact_list))

def delete():
    

# - Implement a CRUD REPL - #

# - Version 3 - #
# - Save the updated Contact List CSV - #