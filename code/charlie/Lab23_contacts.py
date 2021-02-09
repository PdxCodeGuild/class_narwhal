import string

def main():
    translator = str.maketrans('', '', string.punctuation + '""')
    
    contact_list = []
    with open('contact.csv', 'r') as f:
        contacts = f.read()
    
    contacts = contacts.translate(translator)
    keys = contacts[0]
    contacts = str(contacts)
    contacts = contacts.strip()
    contacts = contacts.split(",")

    #contacts.pop(0)
    keys = keys.split(",")
    contacts = [word for word in contacts if word not in keys]
    for contact in contacts:
        entry = {}
        for key in keys:
            entry[key] = contact
        contact_list.append(entry)

    print(contact_list)

main()