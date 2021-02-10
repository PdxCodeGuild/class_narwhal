import string

def main():
   # translator = str.maketrans('', '', string.punctuation)
    
    contact_list = []
    with open('contact.csv', 'r') as f:
        contents = f.read().split('\n')
    
    #contents = contents.translate(translator)
    contents = [word.strip() for word in contents]
    keys = contents[0]
    keys = keys.split(",")
    
    #contacts = contacts.split(",")
    #contacts.pop(0)
    contacts = [word for word in contacts if word not in keys]
    for contact in contacts:
        entry = {}
        for key in keys:
            entry[key] = contact
        contact_list.append(entry)

    print(contact_list)

main()