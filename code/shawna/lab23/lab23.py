with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

    #split headers
    headers = lines[0].split(',')
    h1, h2, h3 = headers[0], headers[1], headers[2]

    #create contacts
    contacts =  []

    #collect each contact in lines and store in contacts
    for contact in lines:
        x = contact.split(',')
        contact = {
            h1: x[0], 
            h2 : x[1], 
            h3 : x[2]
            }
        contacts.append(contact)

def create():
        contact = {
            h1: input('First: '), 
            h2 : input('Last: '), 
            h3 : input('Phone: ')
            }
        contacts.append(contact)


# create()
# print(contacts)

# print(contacts)

def retrieve(contacts):
    target = input("What is the First name of the contact you would like to retrieve?  ")
    for contact in contacts:
        x = contact
        if x.get("First") == target:
            return(x)

# print(retrieve(contacts))

def update_contact(contacts):
    update_contact = retrieve(contacts)
    search = input("Please enter 'First' 'Last' or 'Phone' for the field you would like to update: ")
    change = input(f"That field currently is set to {update_contact.get(search)}. \n What would you like to change it to?  ")
    update_contact[search] = change
    return update_contact

def delete_contact(contacts):
    delete_contact = retrieve(contacts)
    for i, contact in enumerate(contacts):
        if contact == delete_contact:
            del contacts[i]
    print(contacts)

delete_contact(contacts)