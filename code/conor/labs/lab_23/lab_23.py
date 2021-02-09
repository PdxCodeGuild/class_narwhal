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


# print(contact_list)

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
    read = input('Please enter the name of the contact? ')
    for contact in contact_list:
        c = contact
        if c.get("name") == read:
            print(c)

# read(contact_list, header)

def update(contact_list):
    update = read(contact_list)
    contact_to_update = input("Please enter the category you would like to update: ")
    update_contact = input(f"What would you like to change it to?  ")
    update[contact_to_update] = update_contact
    return update_contact

# update(contact_list)

def delete(contact_list):
    delete = input('Which contact would you like to delete? ')
    for i, contact in enumerate(contact_list):
        if contact == delete:
            del contact_list[i]

# delete(contact_list)

# print(contact_list)

# - Implement a CRUD REPL - #

# create = create(contact_list, header)
# read = read(contact_list)
# update = update(contact_list)
# delete = delete(contact_list)

# while True:
#     print('Welcome to your Contacts List!')
#     print("Enter 'quit' if you are finished")
#     task = input("Would you lke to 'create', 'read', 'update', or 'delete' a contact? ")
#     if task == 'quit':
#         print('Have a good day!')
#         break
#     elif task == 'create':
#         create(contact_list, header)
#     elif task == 'read':
#         read(contact_list)
#     elif task == 'update':
#         update(contact_list)
#     elif task == 'delete':
#         delete(contact_list)

# print(contact_list)

# - Version 3 - #
# - Save the updated Contact List CSV - #