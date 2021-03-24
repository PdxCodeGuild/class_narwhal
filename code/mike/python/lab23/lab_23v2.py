'''
Lab 23
Version 2
Contacts List
'''

with open('contacts.csv', 'r') as file: # Opens contacts.csv
    rows = file.read() # reads file as rows
contacts = [] # creates empty list

rows = rows.split('\n') # separates rows with line break
header = rows[0].split(',') # Identifies the top row as header

# starts list of contacts on the first row after header
for x in range(1, len(rows)):
    row = rows[x].split(',')
    contact = dict(zip(header, row))
    contacts.append(contact)


# create contact
def contact_new():
    new_contact = {} # empty dictionary for contact
    for info in header: 
        new_contact[info] = input(f'Enter contact\'s {info}: ') # user inputs the contact information based on the header value
    contacts.append(new_contact) # after loop, adds the contact list to the list of dictionaries


# looks up contact
def contact_lookup():
    for category in header:
        category = input(f'What category do you want to search by? {header}: ')
        data = input(f'Enter contact\'s {category}: ')
        for contact in contacts:
            if data == contact[category]:
                data = contact['name'], contact['favorite fruit'], contact['favorite color']
                data = ' '.join(data)
                return data


# update contact
def contact_update():
    contact = input('Which contact would you like to update? ')
    category = input(f'Which category do you want to update? {header}: ')
    ind = header.index(category)
    update_info = input(f'What do you want to change {category} to? ')
    for info in contacts:
        if contact == info['name']:
            contact = info['name'], info['favorite fruit'], info['favorite color']
            contact = list(contact)
            contact[ind] = update_info
            contact = tuple(contact)
            contact = ' '.join(contact)
            print(contact)
            return contact


# delete contact
def contact_delete():
    contactDel = input('Which contact would you like to delete? ')
    for ind, contact in enumerate(contacts):
        if contactDel == contact['name']:
            return contacts.pop(ind)




# loop to determine user action
while True:
    action = input('What would you like to do? (new/search/update/delete): ')

    # create new contact
    if action == 'new':
        contact_new()
        break

    # search for contact by name
    elif action == 'search':
        print(contact_lookup())
        break
    
    elif action == 'update':
        contact_update()
        break
        
    elif action == 'delete':
        contact_delete()
        break
        

    # break's loop if "new" or "search" not selected
    else:
        break

print(contacts)
    
