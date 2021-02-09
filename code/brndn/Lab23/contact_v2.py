'''
=-=-= Lab 23 08 Feb 2021 =-=-=
=-=-=-=- Contact List -=-=-=-=
=-=-=- Composer: brndn =-=-=-=
'''

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []

keys = lines.pop(0).split(',')                            #separate header and split on ','s as keys

contact_profiles = [line.split(',') for line in lines]    #separate remaining lines as contact profiles.

for profile in contact_profiles:                          #pair keys with values for each profile
    contacts.append(dict(zip(keys,profile)))              #store each profile as a dictionary

def create_record():
    new_profile = input('\nEnter name, favorite fruit, and favorite color, each separated by a comma(,) without spaces:\n>>> ').split(',') 
    contacts.append(dict(zip(keys,new_profile)))

def retrieve_record():
    name = input('\nContact name: ')
    for index, contact in enumerate(contacts):
        if name in contact['Name']:
            print(f'\n{contacts[index]}')
            return index

def update_record():
    record_to_update = retrieve_record(input('\nContact name: '))
    attribute = input('\nattribute?: ')
    new_value = input(f'\nnew {attribute}?: ')
    contacts[record_to_update][attribute] = new_value

def delete_record():
    record_to_delete = retrieve_record(input('\nContact name: '))
    contacts.pop(record_to_delete)

crud_func = {
    'create': create_record(),
    'retrieve': retrieve_record(),
    'update': update_record(),
    'delete': delete_record(),
}

while True:
    crud = input('\nManage contacts; ("Exit" to quit)\n"Create", "Retrieve", "Update", "Delete"\n>>> ').lower()
    if crud == 'exit':
        break

    crud_func[crud]


