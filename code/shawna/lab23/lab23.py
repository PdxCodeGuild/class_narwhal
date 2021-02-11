def load_csv():
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
        return contacts

def save_csv(contacts):
    with open('contacts.csv', 'w') as file:
        for contact in contacts:
            file.write(",".join(contact.values())+ "\n")

def create(contacts):
        contact = {
            "First" : input('First: '), 
            "Last" : input('Last: '), 
            "Phone" : input('Phone: ')
            }
        contacts.append(contact)
        return contacts

def retrieve(contacts):
    target = input("What is the First name of the contact you would like to retrieve?  ")
    for contact in contacts:
        x = contact
        if x.get("First") == target:
            return(x)

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
    return(contacts)

def run():
    contacts = load_csv()
    while True:
        x = input("What would you like to do? Please enter a number\n1) Create a contact\n2) Retrieve a contact.\n3) Update a contact\n4) Delete a contact\n5) Quit (Ya, Quitter)\n")
        action= int(x)
        if action == 1:
            print(create(contacts))
        elif action == 2:
            print(retrieve(contacts))
        elif action == 3:
            print(update_contact(contacts))
        elif action == 4:
            print(delete_contact(contacts))
        elif action == 5:
            save_csv(contacts)
            break
        else: 
            print("That is not a valid selection. Try again.")

run()